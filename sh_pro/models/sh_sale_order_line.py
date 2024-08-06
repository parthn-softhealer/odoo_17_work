from odoo import fields , models , api 


class ShSaleOrderLine(models.Model):
    _name = "sh.sale.order.line"
    _rec_name ="sale_order_rec_id"

    order_id = fields.Many2one("sh.sale.order")
    product_id = fields.Many2one("sh.product.product",string = "Select Product")
    qty = fields.Integer(string = "Enter Qty")
    price = fields.Float(string = "Enter Price")
    tax_id = fields.Many2one("sh.account.tax", string = "Select Tax")
    total_cost = fields.Float(compute="_compute_total_cost")
    tax_rate = fields.Float(related="tax_id.tax_value")
    sale_order_rec_id = fields.Char(compute="compute_rec_name")

    def compute_rec_name(self):
        self.sale_order_rec_id = "S00"+str(self.id)

    @api.depends("price" , 'qty' , 'tax_id' , 'tax_rate')
    def _compute_total_cost(self):
        for record in self : 
            record.total_cost = ((record.tax_rate * record.price * record.qty)/100)+(record.qty * record.price) 