from odoo import models, fields, api


class ShModel(models.Model):

    _name = "new.model"
    _inherit = ["mail.thread", "mail.activity.mixin"]
    _description = "Company Example"

    name = fields.Char(string="Name", required=True)
    email = fields.Char(string="Email")
    user_id = fields.Many2one("res.users", string="User")

    def action_send_email(self):
        mail_template = self.env.ref("practice.sh_student_mail_view")
        mail_template.send_mail(self.id, force_send=True)
