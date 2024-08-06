from odoo import fields,models,api

class ShTopic(models.Model):
    _name="sh.topic"
    _description="Topic of subject"
    

    course_name=fields.Many2one("sh.student")
    course_id=fields.Many2one("sh.student")
    name=fields.Char(string="Topic")
    
   