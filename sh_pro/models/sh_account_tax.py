from odoo import fields , models , api


class ShAccountTax(models.Model):
    _name = "sh.account.tax"
    _rec_name = "tax_value"
    
    tax_value = fields.Float(string = "Enter Tax Name")




