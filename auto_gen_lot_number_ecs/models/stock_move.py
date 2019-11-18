from odoo import models,api,fields
import datetime
import time
from datetime import datetime, timedelta
from dateutil.relativedelta import relativedelta


class stock_move(models.Model):
    _inherit="stock.move"

    def _prepare_move_line_vals(self, quantity=None, reserved_quant=None):
        result = super(stock_move, self)._prepare_move_line_vals()
        if self.purchase_line_id:
            if self.product_id.tracking == 'lot':
                auto_gen_lot_number = self.env['ir.config_parameter'].sudo().get_param('auto_gen_lot_number_ecs.auto_generate_lot_based_on')
                if auto_gen_lot_number == 'schedule_date':
                    scheduled_date = datetime.strptime(self.picking_id.scheduled_date,"%Y-%m-%d %H:%M:%S")
                    date = datetime.strftime(scheduled_date,'%Y%m%d')
                else:
                    date = datetime.now().strftime('%Y%m%d')
                counter = 1
                lot_id_name=date
                lot_ids=self.env['stock.production.lot'].search([('product_id','=',self.product_id.id),('name',"ilike",date)])
                for lot in lot_ids:
                    counter+=1
                    lot_id_name=date+str(counter)
                vals={
                    "product_id":self.product_id.id,
                    "name":lot_id_name
                    }
                lot_id = self.env['stock.production.lot'].create(vals)
                result = dict(
                            result,
                            lot_id=lot_id.id,
                            qty_done=self.product_uom_qty)       
        return result
# class stock_picking_inhe(models.Model):
#     _inherit="stock.picking"
#     
#     @api.multi
#     def process_done_picking(self,move_line):
#         counter=1
#         if move_line.purchase_line_id:#and not move_line.push_rule_id:
#             lot_ids=self.env['stock.production.lot'].search([('product_id','=',move_line.product_id.id),('name',"ilike",datetime.datetime.now().strftime('%y%m%d'))])
#             for lot in lot_ids:
#                 counter+=1
#             lot_id_name=datetime.datetime.now().strftime('%y%m%d')+str(counter)
#             vals={
#                 "product_id":move_line.product_id.id,
#                 "name":lot_id_name
#                 }
#             lot_id = self.env['stock.production.lot'].create(vals)
#         for move_line_inner in move_line.move_line_ids:
#             if move_line.purchase_line_id:# and not move_line.push_rule_id:
#                 if not move_line_inner.lot_name:
#                     move_line_inner.write({'lot_id':lot_id.id}) 
#             if move_line_inner.qty_done == 0:
#                 if not move_line_inner.location_id.is_input_location:
#                     move_line_inner.qty_done=move_line_inner.product_uom_qty
#                 else:
#                     available_qty = move_line_inner.product_id.with_context(location=move_line_inner.location_id.id).qty_available
#                     move_line_inner.qty_done=available_qty
#                 
#     @api.multi
#     def button_validate(self):   
#         for move_line in self.move_lines:            
#             if move_line.picking_id.check_ids and move_line.picking_id.check_ids.filtered(lambda qc:qc.quality_state=='fail' and qc.product_id):
#                 for quality_check in move_line.picking_id.check_ids.filtered(lambda qc:qc.quality_state=='fail' and qc.product_id):
#                     if move_line.product_id.id == quality_check.product_id.id:
#                         continue
#                     else:
#                         self.process_done_picking(move_line)
# #                 else:
# #                     self.process_done_picking(move_line)                                        
#             else:
#                 self.process_done_picking(move_line)
#         res=super(stock_picking_inhe,self).button_validate()
#         return res
