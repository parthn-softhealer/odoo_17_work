from odoo import models , fields

class ShSaleOrder(models.Model):
    _inherit = "sale.order"
    
    my_temp= fields.Char(string = "Enter Temp Name")


    
