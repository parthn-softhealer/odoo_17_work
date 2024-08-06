from odoo import fields, models, api
from datetime import datetime
from odoo.exceptions import UserError, ValidationError


class ShStudent(models.Model):
    _name = "sh.student"
    _description = "this is student details "
    _rec_name = "identification_number"
    _inherit = ["mail.thread", "mail.activity.mixin"]

    identification_number = fields.Char(string="Enrollment Number")
    student_id = fields.Many2one("res.partner", string="student name", required=True)
    student_mobile = fields.Char(string="Studetn Mobile", required=True)
    student_email = fields.Char(string="Student Email", required=True)
    course_name = fields.Many2one("sh.course")
    course_id = fields.Many2one("sh.course")
    teacher_id = fields.Many2one("sh.teacher")

    # teacher_id=fields.One2many("sh.course","teacher_ids",srting="Suggestation")
    attadance = fields.One2many("sh.attadance", "attadance_id", string="Attadance")
    # join_date=fields.Date("joinning date")
    concate = fields.Char(string="Concate Name")
    # suggestion = fields.Many2many(related='course_id.teacher_ids')
    suggestion = fields.Many2many("sh.teacher", string="Suggested Teacher")

    suggestTopic = fields.Many2many("sh.topic", string="Topic Suggest")

    _sql_constraints = [
        ("unique_name", "unique(student_email)", "The name must be unique!")
    ]

    @api.model_create_multi
    def create(self, vals_list):
        print("..................self", self)
        print(".......vals_list:", vals_list)
        seq = self.env["ir.sequence"].next_by_code("sh.student") or ("New")
        for record in vals_list:
            record["identification_number"] = seq
        lines = super().create(vals_list)
        return lines

    def write(self, vals):
        result = super().write(vals)
        return result

    def suggest(self):
        self.suggestion = self.env["sh.teacher"].search(
            [("course_id", "=", self.course_id.id)]
        )
        print("............", self, self.suggestion)

    def TopicSuggation(self):
        self.suggestTopic = self.env["sh.topic"].search(
            [("course_id", "=", self.course_id.id)]
        )
        print(f"\n\n\n>>> 38 | :{self.course_id.id} ")
        print(f"\n\n\n>>> 41 | {self.suggestTopic}:  ")

    @api.constrains("student_mobile")
    def _check_student_mobile(self):
        for rec in self:
            if len(rec.student_mobile) != 10:
                raise ValidationError("Mobile number must have 10 digit only!")

    @api.model
    def test_cron(self):
        print("\n\n\n-----------------------")
        print("Cron Executed Succesfully")
        print("-----------------------\n\n\n")


class ResPartner(models.Model):
    _inherit = "res.partner"

    @api.model
    def _name_search(
        self,
        name="",
        args=None,
        operator="ilike",
        limit=100,
        name_get_uid=None,
        order=None,
    ):
        args = list(args or [])
        if name:
            args += [
                "|",
                "|",("name", operator, name),("email", operator, name),("phone", operator, name),
            ]
        return self._search(args, limit=limit, access_rights_uid=name_get_uid)
