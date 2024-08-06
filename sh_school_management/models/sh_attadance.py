from odoo import fields,models

class ShAttadance(models.Model):
    _name="sh.attadance"
    _description="Attadance fields "


    check_in=fields.Datetime(string="check in ")
    check_out=fields.Datetime(string="check out ")
    attadance_id=fields.Many2one("sh.student")


    