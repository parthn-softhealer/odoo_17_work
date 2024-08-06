from odoo import fields , models 

class ShOrderLine(models.Model):
    _inherit = "sale.order.line"

    my_temp = fields.Char(string = "Enter Temp Name")
