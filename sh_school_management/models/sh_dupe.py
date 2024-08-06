from odoo import fields,models,api

class ShDupe(models.Model):
    _name="sh.dupe"
    _description="dupe"


    name_id=fields.Many2one("sh.fees",string="Name")
    enroll=fields.Char(related='name_id.enroll',string="enroll")
    subject=fields.Char(related='name_id.subject',string="Subject")
    

    person_id = fields.Many2one('res.partner')
    person_mobile = fields.Char(related="person_id.mobile")
    person_email = fields.Char(related="person_id.email")
    person_hobbies = fields.Many2many(related="person_id.category_id")