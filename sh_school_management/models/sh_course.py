from odoo import fields, models, api


class ShCourse(models.Model):
    _name = "sh.course"
    _description = "This is course model"
    _rec_name = "course_name"

    student_id = fields.Many2one("sh.student")
    course_name = fields.Char(string="Course Name", required=True)
    course_description = fields.Text(string="Course Description")
    start_date = fields.Date(string="Course Start Date")
    course_price = fields.Float(string="Course Fees", default=1500, readonly=True)
    course_hours = fields.Integer(string="Course Hours")

    max_student = fields.Integer(string="Maximum Students", compute="Max")
    image = fields.Binary(string="Image")
    student_ids = fields.One2many("sh.student", "course_id")
    teacher_ids = fields.One2many("sh.teacher", "course_id")
    num = fields.Integer(string="Total no of student")
    topic_ids = fields.Many2many("sh.topic", string="Topic")

    def ButtonObject(self):
        print(self.student_ids)
        for stu in self.student_ids:
            print(f"{stu.id}", "name: ", stu.student_name)
        for tea in self.teacher_ids:
            print(f"{tea.id} name: {tea.teacher_name}")
        print(".................../n/n/n/n/", "hi shruti")

    # @api.model_create_multi
    # def create(self, vals_list):
    #     print(".......",vals_list)
    #     lines = super().create(vals_list)
    #     print("...........len.........",len(vals_list))
    #     return lines

    @api.depends("student_ids")
    def Max(self):
        print(f"\n\n\n>>> 38 | {self}:  ")
        for i in self:
            i.max_student = len(i.student_ids)
            # print(f'\n\n\n>>> 40 | {i.student_ids.student_name}:  ')
