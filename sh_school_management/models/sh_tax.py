from odoo import fields,models 

class ShTax(models.Model):
    _name="sh.tax"
    _description="tax"
    _rec_name="tax"


    tax=fields.Integer(string="Tax")