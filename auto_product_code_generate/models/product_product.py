# -*- coding: utf-8 -*-
# Part of Odoo. See COPYRIGHT & LICENSE files for full copyright and licensing details.

from odoo import api, fields, models


class ProductProduct(models.Model):
    _inherit = 'product.product'

    @api.multi
    def generate_default_code(self, vals={}):
        get_param = self.env['ir.config_parameter'].sudo().get_param
        product_name = get_param('auto_product_code_generate.product_name')
        use_attribute = get_param('auto_product_code_generate.use_attribute')
        attributes = get_param("auto_product_code_generate.attributes")
        use_category = get_param("auto_product_code_generate.use_category")
        category = get_param('auto_product_code_generate.category')
        join = get_param('auto_product_code_generate.join')
        change_case = get_param('auto_product_code_generate.change_case')
        sequence = get_param('auto_product_code_generate.sequence')
        default_code_list = []
        if not vals:
            # name code
            name_default_code = ""
            if product_name == '1st_of_each':
                words = self.name.split()
                first_letters = [word[0] for word in words]
                name_default_code += "".join(first_letters)
            elif product_name == '2_letters':
                name_default_code += self.name[:2]
            elif product_name == '3_letters':
                name_default_code += self.name[:3]
            elif product_name == '4_letters':
                name_default_code += self.name[:4]
            default_code_list.append(name_default_code.strip())

            # category code
            if use_category:
                if self.categ_id:
                    categ_default_code = ""
                    category_name = self.categ_id.name
                    if category == '2_letters':
                        categ_default_code += category_name[:2]
                    elif category == '3_letters':
                        categ_default_code += category_name[:3]
                    elif category == '4_letters':
                        categ_default_code += category_name[:4]
                    default_code_list.append(categ_default_code.strip())

            # Attributes code
            if use_attribute:
                attr_default_code = ""
                if self.attribute_value_ids:
                    for value_id in self.attribute_value_ids:
                        if attributes == '2_letters':
                            attr_default_code += value_id.name[:2]
                        elif attributes == '3_letters':
                            attr_default_code += value_id.name[:3]
                        elif attributes == '4_letters':
                            attr_default_code += value_id.name[:4]
                    default_code_list.append(attr_default_code.replace(" ", ""))
        else:
            if not vals.get('product_tmpl_id'):
                # name code
                name_default_code = ""
                if vals.get('name', False):
                    if product_name == '1st_of_each':
                        words = vals.get('name').split()
                        first_letters = [word[0] for word in words]
                        name_default_code += "".join(first_letters)
                    elif product_name == '2_letters':
                        name_default_code += vals.get('name')[:2]
                    elif product_name == '3_letters':
                        name_default_code += vals.get('name')[:3]
                    elif product_name == '4_letters':
                        name_default_code += vals.get('name')[:4]

                    default_code_list.append(name_default_code.strip())

                # category code
                if use_category:
                    if vals.get('categ_id'):
                        categ_default_code = ""
                        categ_id = self.env['product.category'].browse(vals['categ_id'])
                        if categ_id:
                            if category == '2_letters':
                                categ_default_code += categ_id.name[:2]
                            elif category == '3_letters':
                                categ_default_code += categ_id.name[:3]
                            elif category == '4_letters':
                                categ_default_code += categ_id.name[:4]
                            default_code_list.append(categ_default_code.strip())

                # Attributes code
                if use_attribute:
                    attr_default_code = ""
                    if self.attribute_value_ids:
                        for value_id in self.attribute_value_ids:
                            if attributes == '2_letters':
                                attr_default_code += value_id.name[:2]
                            elif attributes == '3_letters':
                                attr_default_code += value_id.name[:3]
                            elif attributes == '4_letters':
                                attr_default_code += value_id.name[:4]
                    if vals.get('attribute_value_ids', False):
                        for value in vals['attribute_value_ids']:
                            attribute_value_id = self.env['product.attribute.value'].browse(value[1])
                            if attribute_value_id:
                                if attributes == '2_letters':
                                    attr_default_code += attribute_value_id.name[:2]
                                elif attributes == '3_letters':
                                    attr_default_code += attribute_value_id.name[:3]
                                elif attributes == '4_letters':
                                    attr_default_code += attribute_value_id.name[:4]
                    attr_default_code and default_code_list.append(attr_default_code.replace(" ", ""))

            elif vals.get('product_tmpl_id'):
                product_tmpl_id = self.env['product.template'].browse(vals['product_tmpl_id'])
                name_default_code = ""
                if product_name == '1st_of_each':
                    words = product_tmpl_id.name.split()
                    first_letters = [word[0] for word in words]
                    name_default_code += "".join(first_letters)
                elif product_name == '2_letters':
                    name_default_code += product_tmpl_id.name[:2]
                elif product_name == '3_letters':
                    name_default_code += product_tmpl_id.name[:3]
                elif product_name == '4_letters':
                    name_default_code += product_tmpl_id.name[:4]

                default_code_list.append(name_default_code.strip())

                # category code
                if use_category:
                    if product_tmpl_id.categ_id:
                        categ_default_code = ""
                        category_name = product_tmpl_id.categ_id.name
                        if category == '2_letters':
                            categ_default_code += category_name[:2]
                        elif category == '3_letters':
                            categ_default_code += category_name[:3]
                        elif category == '4_letters':
                            categ_default_code += category_name[:4]
                        default_code_list.append(categ_default_code.strip())

                # Attributes code
                if use_attribute:
                    attr_default_code = ""
                    attribute_value_ids = vals.get('attribute_value_ids')
                    if attribute_value_ids:
                        if attributes == '2_letters':
                            for rec in attribute_value_ids:
                                for value_id in rec[2]:
                                    attribute_value_id = self.env['product.attribute.value'].browse(value_id)
                                    attr_default_code += attribute_value_id.name[:2]
                        elif attributes == '3_letters':
                            for rec in attribute_value_ids:
                                for value_id in rec[2]:
                                    attribute_value_id = self.env['product.attribute.value'].browse(value_id)
                                    attr_default_code += attribute_value_id.name[:3]
                        elif attributes == '4_letters':
                            for rec in attribute_value_ids:
                                for value_id in rec[2]:
                                    attribute_value_id = self.env['product.attribute.value'].browse(value_id)
                                    attr_default_code += attribute_value_id.name[:4]
                        attr_default_code and default_code_list.append(attr_default_code.replace(" ", ""))

        # sequence code
        sequence_default_code = ""
        if sequence:
            sequence_default_code += sequence
            default_code_list.append(sequence_default_code)

        # join code
        if join == 'hyphen':
            default_code = "-".join(default_code_list)
        elif join == 'underscore':
            default_code = "_".join(default_code_list)
        else:
            default_code = "".join(default_code_list)

        # convert case
        if change_case == 'title':
            default_code = default_code.title()
        elif change_case == 'lower':
            default_code = default_code.lower()
        elif change_case == 'upper':
            default_code = default_code.upper()
        return default_code

    @api.model
    def create(self, vals):
        res = super(ProductProduct, self).create(vals)
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
            res.update({'default_code':self.generate_default_code(vals=vals) + str(join_sign) + str(res.id)})

        if vals.get('default_code'):
            res.update({'default_code': vals['default_code']})

        return res

    @api.multi
    def write(self, vals):
        if not vals.get('name', False):
            vals['name'] = self.name
        if not vals.get('categ_id', False):
            vals['categ_id'] = self.categ_id.id
        if not vals.get('default_code'):
            vals.update({
                'default_code': self.generate_default_code(vals=vals) + str(self.id)
            })
        res = super(ProductProduct, self).write(vals)
        return res

# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4: