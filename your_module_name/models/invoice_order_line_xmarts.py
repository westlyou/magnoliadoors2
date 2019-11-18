from odoo import api, fields, models, _

class nuevo(models.Model):
    _inherit = 'account.invoice.line'
    x_invquantityS= fields.Float(related="sale_line_ids.x_quantity",string='x_invquantity ')
    x_invquantityC= fields.Float(related="purchase_line_id.x_quantity",string='x_invquantity ')


    quantity=fields.Float(string='Quantity',readonly=1,compute='myfunction2')
    @api.onchange('name','x_studio_pieces','x_studio_pieces_1')
    def myfunction2(self):
    	for record in self:
            if(record.x_invquantityS)!=0:
                record[("quantity")]=record.x_invquantityS
            elif(record.x_invquantityC)!=0:
                record[("quantity")]=record.x_invquantityC
            elif(record.x_studio_pieces)!=0:
                record[("quantity")]=record.self
            else:
                record[("quantity")]=record.self
