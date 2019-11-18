# -*- coding: utf-8 -*-

from odoo import fields, models, _

class AccountMoveLine(models.Model):
    _inherit = 'account.move.line'

    user_id = fields.Many2one('res.users', string='Salesperson', related="invoice_id.user_id", store=True)