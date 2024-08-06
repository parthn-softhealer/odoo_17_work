from odoo import fields, models 


class WizardSaleOrder(models.TransientModel):
    _name = 'wizard.sale.order'

    name = fields.Char()
    