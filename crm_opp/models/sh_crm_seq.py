from odoo import models, fields, api


class ShCRMSeq(models.Model):
    _inherit = "crm.lead"

    seq = fields.Char(string="Sequence")

    @api.model_create_multi
    def create(self, vals_list):
        print("..................self", self)
        print(".......vals_list:", vals_list)
        seq = self.env["ir.sequence"].next_by_code("crm.seq")
        for record in vals_list:
            record["seq"] = seq
        lines = super().create(vals_list)
        return lines
