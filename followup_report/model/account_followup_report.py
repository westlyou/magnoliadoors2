# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

from datetime import datetime, timedelta
from odoo import models, fields, api
from odoo.tools.misc import formatLang, format_date
from odoo.tools.translate import _
from odoo.tools import append_content_to_html, DEFAULT_SERVER_DATE_FORMAT
from odoo.exceptions import UserError

class AccountFollowupReport(models.AbstractModel):
    _inherit = "account.followup.report"

    @api.model
    def send_email(self, options):
        """
        Send by mail the followup to the customer
        """
        partner = self.env['res.partner'].browse(options.get('partner_id'))
        email = self.env['res.partner'].browse(partner.address_get(['invoice'])['invoice']).email
        options['keep_summary'] = True
        if email and email.strip():
            # When printing we need te replace the \n of the summary by <br /> tags
            body_html = self.with_context(print_mode=True, mail=True, lang=partner.lang or self.env.user.lang).get_html(options)
            start_index = body_html.find(b'<span>', body_html.find(b'<div class="o_account_reports_summary">'))
            end_index = start_index > -1 and body_html.find(b'</span>', start_index) or -1
            if end_index > -1:
                replaced_msg = body_html[start_index:end_index].replace(b'\n', b'<br />')
                body_html = body_html[:start_index] + replaced_msg + body_html[end_index:]
            msg = _('Follow-up email sent to %s') % email
            msg += '<br>' + body_html.decode('utf-8')
            msg_id = partner.message_post(body=msg)
            
            if partner and partner.followup_email:
                
                followup_email = self.env['mail.mail'].create({
                    'mail_message_id': msg_id.id,
                    'subject': _('%s Payment Reminder') % (self.env.user.company_id.name) + ' - ' + partner.name,
                    'body_html': append_content_to_html(body_html, self.env.user.signature or '', plaintext=False),
                    'email_from': self.env.user.email or '',
                    'email_to': partner.followup_email,
                    'body': msg,
                })
                print ('followup_email ', followup_email )
            else:
                email = self.env['mail.mail'].create({
                    'mail_message_id': msg_id.id,
                    'subject': _('%s Payment Reminder') % (self.env.user.company_id.name) + ' - ' + partner.name,
                    'body_html': append_content_to_html(body_html, self.env.user.signature or '', plaintext=False),
                    'email_from': self.env.user.email or '',
                    'email_to': email,
                    'body': msg,
                })
            partner.message_subscribe([partner.id])
            return True
        raise UserError(_('Could not send mail to partner because it does not have any email address defined'))
