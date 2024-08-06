from odoo import fields,models

class ShTeacher(models.Model):
    _name="sh.teacher"
    _description="details of teacher"
    _rec_name="teacher_name"

    teacher_name=fields.Char(string="Teacher name")
    course_id=fields.Many2one("sh.course")
    sub_exp_ids=fields.One2many("sh.teacher.experience","teacher_id",string="Subject Experience")
    attadance_ids=fields.One2many("sh.attadance","attadance_id",string="Teacher Attadance")

    def teacher(self):
        print(".............................",self)