# -*- coding: utf-8 -*-
# Part of Odoo. See COPYRIGHT & LICENSE files for full copyright and licensing details.

from odoo import models, api, fields, _
from odoo.exceptions import UserError


class MultiProductInternalReference(models.TransientModel):
    _name = "multi.product.internal.reference"

    overwrite = fields.Boolean("Overwrite Existing Internal Reference.")

    @api.multi
    def create_internal_references(self):
        context = dict(self._context or {})
        active_ids = context.get('active_ids', []) or []
        product_ids = self.env['product.product'].browse(active_ids)
        for record in product_ids:
            if not self.overwrite and not record.default_code or self.overwrite:
                get_param = self.env['ir.config_parameter'].sudo().get_param
                join = get_param('auto_product_code_generate.join')
                sequence = get_param('auto_product_code_generate.sequence')
                join_sign = ''
                if not sequence:
                    if join == 'hyphen':
                        join_sign = "-"
                    elif join == 'underscore':
                        join_sign = "_"
                    else:
                        join_sign = ""

                    record.write({
                    'default_code': record.generate_default_code() + str(join_sign) + str(record.id),
                })
                else:
                    record.write({
                    'default_code': record.generate_default_code() + str(record.id),
                })

        return {'type': 'ir.actions.act_window_close'}

# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4: