from odoo import fields , models  ,   api

class ShSchoolStudent(models.Model):
    _name = "sh.school.student"

    name = fields.Char()
    gender = fields.Selection([('male', 'Male'), ('female', 'Female')], string="Gender")


        
    def unlink(self):
        print(f'\n\n\n>>> 63 | {self}:  ')
        res = super().unlink()
        print(f'\n\n\n>>> 65 | {self}:  ')
        print("type : " , type(res))
        return res

    @api.returns('self', lambda value: value.id)
    def copy(self, default=None):
        print(f'\n\n\n>>> 70 copy| {self}:  ')
  
        clone = super().copy(default)
        print(f'\n\n\n>>> 73 copy| {self}:  ')
        print("type : " , type(clone))
       
        return clone
