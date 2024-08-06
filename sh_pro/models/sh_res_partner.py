from odoo import fields , models 


class ShResPartner(models.Model):
    _name = "sh.res.partner"
    
    name = fields.Char(string = "Enter Name")
    city = fields.Char(string = "Enter city")