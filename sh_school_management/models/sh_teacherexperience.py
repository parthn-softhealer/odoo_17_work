
from odoo import fields, models

class ShTeacherExperience(models.Model):
    _name = "sh.teacher.experience"
    _description = "to show teacher experience"

    teacher_id = fields.Many2one("sh.teacher", string="Teacher", required=True)
    course_id = fields.Many2one("sh.course", string="Course", required=True)
    year_exp = fields.Integer(string="Experience")
