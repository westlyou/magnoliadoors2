# -*- coding: utf-8 -*-
# Part of Odoo. See COPYRIGHT & LICENSE files for full copyright and licensing details.

from odoo import api, fields, models


class ResConfigSettings(models.TransientModel):
    _inherit = 'res.config.settings'

    product_name = fields.Selection([
        ('1st_of_each', '1st letter of Each word.'),
        ('2_letters', 'Two letters (1st)'),
        ('3_letters', 'Three letters (1st)'),
        ('4_letters', 'Four letters (1st)')
        ], string="Product Name", default="1st_of_each")
    use_attribute = fields.Boolean("Use Attributes")
    attributes = fields.Selection([
        ('2_letters', 'Two letters (1st)'),
        ('3_letters', 'Three letters (1st)'),
        ('4_letters', 'Four letters (1st)')
        ], string="Attributes", default="2_letters")
    use_category = fields.Boolean("Use Category")
    category = fields.Selection([
        ('2_letters', 'Two letters (1st)'),
        ('3_letters', 'Three letters (1st)'),
        ('4_letters', 'Four letters (1st)')
        ], string="Category", default="2_letters")
    join = fields.Selection([
        ('hyphen', 'Hyphen(-)'),
        ('underscore', 'Underscore( _ )'),
        ('no_symbol', 'Without Symbol')
        ], string="Join Using", default="hyphen")
    change_case = fields.Selection([
        ('title', 'Titile'),
        ('lower', 'Lower'),
        ('upper', 'Upper')
        ], string="Convert Case", default="upper")
    sequence = fields.Char(string="Sequence", default="00")

    @api.model
    def get_values(self):
        res = super(ResConfigSettings, self).get_values()
        ICPSudo = self.env['ir.config_parameter'].sudo()
        product_name = ICPSudo.get_param('auto_product_code_generate.product_name')
        use_attribute = ICPSudo.get_param('auto_product_code_generate.use_attribute')
        attributes = ICPSudo.get_param("auto_product_code_generate.attributes")
        use_category = ICPSudo.get_param("auto_product_code_generate.use_category")
        category = ICPSudo.get_param('auto_product_code_generate.category')
        join = ICPSudo.get_param('auto_product_code_generate.join')
        change_case = ICPSudo.get_param('auto_product_code_generate.change_case')
        sequence = ICPSudo.get_param('auto_product_code_generate.sequence')

        res.update(
            product_name=product_name,
            use_attribute=use_attribute,
            attributes=attributes,
            use_category=use_category,
            category=category,
            join=join,
            change_case=change_case,
            sequence=sequence
        )
        return res

    @api.multi
    def set_values(self):
        super(ResConfigSettings, self).set_values()
        ICPSudo = self.env['ir.config_parameter'].sudo()
        ICPSudo.set_param('auto_product_code_generate.product_name', self.product_name)
        ICPSudo.set_param("auto_product_code_generate.use_attribute", self.use_attribute)
        ICPSudo.set_param("auto_product_code_generate.attributes", self.attributes)
        ICPSudo.set_param("auto_product_code_generate.use_category", self.use_category)
        ICPSudo.set_param('auto_product_code_generate.category', self.category)
        ICPSudo.set_param('auto_product_code_generate.join', self.join)
        ICPSudo.set_param('auto_product_code_generate.change_case', self.change_case)
        ICPSudo.set_param('auto_product_code_generate.sequence', self.sequence)

# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4: