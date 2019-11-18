from odoo import api, fields, models, _

class nuevo(models.Model):
    _inherit = 'sale.order.line'
    altura=fields.Float(default='1',string='Height')
    ancho = fields.Float(default='1',string='Width')
    piezas=fields.Float(default='0',string='Pieces')
    product_uom_qty=fields.Float(string='Cantidad',store=True,readonly=1)
    Custom=fields.Boolean(store='false')
    hide = fields.Boolean(string='Hide', compute="_compute_hide")
    x_quantity =fields.Float(string='x_quantity2',readonly=1,store=True)

	
    @api.onchange('Custom')
    def _compute_hide(self):
        for record in self:
            if (record.Custom) == True:
                record[("hide")]=False
            else:
                record[("hide")]= True

    @api.onchange('altura','ancho','piezas','product_id','hide','price_unit')
    def myfunction(self):
        for record in self:
            if (record.is_downpayment) is True:
                pass
            elif (record.Custom) == True :
            	record[("product_uom_qty")]= (record.altura * record.ancho *record.piezas)/144
            else:
                record[("product_uom_qty")]= record.piezas
                record[("altura")]= 1
                record[("ancho")]= 1
