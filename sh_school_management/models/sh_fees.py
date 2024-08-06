from odoo import fields, models, api


class ShFees(models.Model):
    _inherit = "sh.student"

    @api.model
    def name_search(
        self,
        student_name,
        student_mobile,
        args=None,
        operator="ilike",
        limit=100,
        name_get_uid=None,
    ):
        if not args:
            args = []
        if student_name:
            args = [
                "|",
                ("student_name", operator, student_name),
                ("student_mobile", operator, student_mobile),
            ] + args

        print("\n\n\nargs : ", args)
        return self._search(args, limit=limit, access_rights_uid=name_get_uid)
