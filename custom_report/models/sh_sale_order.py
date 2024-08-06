from odoo import fields , models 


class ShSaleOrder(models.Model):
    _inherit = 'sale.order'

    def action_confirm(self):
        print("---------------------")
        print("Self : " , self)
        
        super().action_confirm()
        print("---------------------")
