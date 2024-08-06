from odoo import fields , models 


class ShProductProduct(models.Model):
    _name = "sh.product.product"
    
    name = fields.Char(string = "Enter Product Name")