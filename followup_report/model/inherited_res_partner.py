from odoo import fields, models

class ResPartner(models.Model):
    _inherit = "res.partner"

    followup_email = fields.Char('Follow Up Email')
    