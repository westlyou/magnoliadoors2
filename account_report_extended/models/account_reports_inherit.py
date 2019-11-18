from odoo.addons.account_reports.models.account_report import AccountReport as BaseAccountReport

class AccountReports(BaseAccountReport):

    def get_report_informations(self, options):
        '''
        return a dictionary of informations that will be needed by the js widget, manager_id, footnotes, html of report and searchview, ...
        '''
        options = self._get_options(options)
        # apply date and date_comparison filter
        self._apply_date_filter(options)

        searchview_dict = {'options': options, 'context': self.env.context}
        # Check if report needs analytic
        if options.get('analytic_accounts') is not None:
            searchview_dict['analytic_accounts'] = self.env.user.id in self.env.ref('analytic.group_analytic_accounting').users.ids and [(t.id, t.name) for t in self.env['account.analytic.account'].search([])] or False
            options['selected_analytic_account_names'] = [self.env['account.analytic.account'].browse(int(account)).name for account in options['analytic_accounts']]
        if options.get('analytic_tags') is not None:
            searchview_dict['analytic_tags'] = self.env.user.id in self.env.ref('analytic.group_analytic_tags').users.ids and [(t.id, t.name) for t in self.env['account.analytic.tag'].search([])] or False
            options['selected_analytic_tag_names'] = [self.env['account.analytic.tag'].browse(int(tag)).name for tag in options['analytic_tags']]
        if options.get('partner'):
            partners = self.env['account.move.line'].read_group([('partner_id', '!=', False)], ['partner_id'], ['partner_id'])
            searchview_dict['res_partners'] = [partner['partner_id'] for partner in partners] or False # list of tuple(id, name)
            searchview_dict['res_partner_categories'] = [(category.id, category.name) for category in self.env['res.partner.category'].search([])] or False
            options['selected_partner_ids'] = [self.env['res.partner'].browse(int(partner)).name for partner in options['partner_ids']]
            options['selected_partner_categories'] = [self.env['res.partner.category'].browse(int(category)).name for category in options['partner_categories']]
        if options.get('users'):
            users = self.env['account.move.line'].read_group([('user_id', '!=', False)], ['user_id'], ['user_id'])
            searchview_dict['salesperson'] = [user['user_id'] for user in users] or False  # list of tuple(id, name)
            options['selected_user_ids'] = [
                self.env['res.users'].browse(int(user)).name for user in options['user_ids']]

        # Check whether there are unposted entries for the selected period or not (if the report allows it)
        if options.get('date') and options.get('all_entries') is not None:
            date_to = options['date'].get('date_to') or options['date'].get('date') or fields.Date.today()
            period_domain = [('state', '=', 'draft'), ('date', '<=', date_to)]
            options['unposted_in_period'] = bool(self.env['account.move'].search_count(period_domain))

        report_manager = self._get_report_manager(options)
        info = {'options': options,
                'context': self.env.context,
                'report_manager_id': report_manager.id,
                'footnotes': [{'id': f.id, 'line': f.line, 'text': f.text} for f in report_manager.footnotes_ids],
                'buttons': self._get_reports_buttons(),
                'main_html': self.get_html(options),
                'searchview_html': self.env['ir.ui.view'].render_template(self._get_templates().get('search_template', 'account_report.search_template'), values=searchview_dict),
                }
        return info

    BaseAccountReport.get_report_informations = get_report_informations