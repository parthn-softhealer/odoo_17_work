from odoo import fields, models , api

class ShChecking(models.Model) :
    _name = "sh.checking"
    _discription = "checking model"

# ,domain=['|',('person_type','=','student'),('person_type','=','principal')]
    person_id = fields.Many2one('sh.person')
    person_type = fields.Char(compute="_get_person_type_")
    person_mobile = fields.Char(related="person_id.mobile")
    person_email = fields.Char(related="person_id.email")
    person_hobbies = fields.Many2many(related="person_id.hobbies")


    
    @api.depends('person_id')
    def _get_person_type_(self):
        self.person_type = self.person_id.person_type
            