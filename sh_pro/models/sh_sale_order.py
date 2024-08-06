from odoo import fields , models 


class ShSaleOrder(models.Model):
    _name = "sh.sale.order"
    _rec_name = "partner_name"
    
    
    ref_name = fields.Char(string = "Order reference Name")
    order_date = fields.Date(string = "Order Date")
    partner_id = fields.Many2one("sh.res.partner")
    partner_name = fields.Char(related="partner_id.name")
    order_line_ids = fields.One2many("sh.sale.order.line" , "order_id")

    