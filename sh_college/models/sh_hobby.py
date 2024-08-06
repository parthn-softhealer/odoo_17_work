from odoo import models , fields

class ShHobby(models.Model):
    _name = "sh.hobby"
    _discription = "Hobby model"
    _rec_name = "hobby_name"


    hobby_name = fields.Char(string = "Enter Hobbies")
    color_id = fields.Integer(string = "Enter color id")

    