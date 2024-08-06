from odoo import models, fields, api


class ShPurchaseOrder(models.Model):
    _inherit = "purchase.order"

    sequence = fields.Char(string="Sequence")

    @api.model_create_multi
    def create(self, val_list):
        for record in val_list:
            record["name"] = self.env["ir.sequence"].next_by_code(
                "request.for.quotation"
            )
            record["sequence"] = record["name"]
        lines = super().create(val_list)
        return lines

    def button_confirm(self):
        print("self : ", self.name)
        for record in self:
            record["name"] = self.env["ir.sequence"].next_by_code("purchase.order")
        res = super().button_confirm()
        return res
