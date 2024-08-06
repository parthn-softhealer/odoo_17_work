from odoo import fields , models , api
from odoo.exceptions import UserError 

class ShPerson (models.Model) :
    _name = "sh.person"
    
    _description = "This is person model"
    _rec_name = "name"

    name=fields.Char()
    surname=fields.Char()
    display_name=fields.Char()
    person_type=fields.Selection([
        ('principal', 'Principal'),
        ('student' , 'Student'),
        ('faculty' , 'Faculty'),
        ('other','Other' )
        ])
    mobile=fields.Char(default="")
    email=fields.Char()
    city=fields.Char()
    state=fields.Char()
    dob=fields.Date()
    hobbies=fields.Many2many("sh.hobby")
    image = fields.Binary()

    # @api.model_create_multi
    # def create(self,vals_list):
    #     print("..................self",self)
    #     print("..................vals_list:",vals_list)
    #     for record in vals_list:
    #         exist = self.env['res.partner'].search([('phone','=',record['mobile'])])
            
    #         if not exist:
    #             self.env['res.partner'].create({
    #                 'name':record['name'] ,
    #                 'phone':record['mobile'],
    #                 'mobile':record['mobile'],
    #                 'email':record['email']  
    #             })
    #             lines = super().create(vals_list)
    #         else:
    #             raise UserError("User already exist")

    #     return lines


    # def write(self , val_list):
    #     print("-------------------")
    #     print(self)
    #     print(val_list)
    #     print("-------------------")
