# from odoo import fields,models,api

# class SemiWizard(models.TransientModel):
#     _name="sh.semiwizard"
#     _description="semi wizard"


#     name=fields.Char(string="name: ")
#     # id=fields.Integer(string="id: ")
        
#     @api.model_create_multi
#     def create(self, vals_list):
#         print(".......",self)
#         lines = super().create(vals_list)
#         print("......semi wizard",lines.name)
#         # new=super("sh.course").create({
#         #     "course_name": lines.name
#         # })
#         students = self.env['sh.course'].search([('course_name', '!=', lines.name)])
#         print(".........studentid: ",str(students))
#         return lines   
    
#     def write(self,values):
#         print(",.........................",values.name)
#         result=super().write(values)
#         print("..........................",result.name)
#         courses = self.env['sh.course'].search([('course_name', '!=', values.get('name'))])
#         print("..................",courses)
#         # for course in courses:
#         #     course.course_name = values.get('name', course.course_name)
        
#         return result

from odoo import fields, models, api

class SemiWizard(models.TransientModel):
    _name = "sh.semiwizard"
    _description = "semi wizard"

    name = fields.Char(string="Name")
    course_id=fields.Many2one("sh.course",string="course name:")

    @api.model_create_multi
    def create(self, vals_list):
        print(".......", self)
        courses = self.env['sh.course'].search([('id', '=', vals_list[0]['course_id'])])
        print(".........course ids: ", courses.ids)
        courses.write({
            'course_name':vals_list[0]['name']
        })
        lines = super().create(vals_list)
        return lines

    def write(self, values):
        print(".........................", values)
        result = super(SemiWizard, self).write(values)
        print("..........................", result)
        return result
