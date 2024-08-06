from odoo import fields, models, api, Command
from datetime import datetime, timedelta


class SaleOrderOptionInvers(models.Model):
    _name = "sh.invers"

    name = fields.Char(string="Sale Order")
    date = fields.Char(string="Order Date")
    product = fields.Char(string="Product")
    pricelist = fields.Char(string="Pricelist")
    price = fields.Char(string="Price")
    newprice = fields.Float(string="New Price")
    quantity = fields.Char(string="Quantity")
    unit = fields.Char(string="Unit")
    discount = fields.Float(string="Discount")
    subtotal = fields.Char(string="Subtotal")
    status = fields.Char(string="Status")
    custom_field_id = fields.Many2one("sale.order", string="Custom Field")
    is_check = fields.Boolean(compute="compute_is_check")

    def compute_is_check(self):
        print("reorder", self.env.company.reorder)
        self.is_check = self.env.company.reorder

    def action_reorder(self):
        print(f"\n\n\n>>> 42 | {self.name}:  ")
        new_sale_order = self.env["sale.order"].create(
            {
                "date_order": fields.Datetime.now(),
                "order_line": [
                    (
                        0,
                        0,
                        {
                            "product_id": self.env["product.product"]
                            .search([("name", "=", self.product)], limit=1)
                            .id,
                            "price_unit": self.price,
                            "product_uom_qty": float(self.quantity),
                            "product_uom": self.env["uom.uom"]
                            .search([("name", "=", self.unit)], limit=1)
                            .id,
                            "discount": self.discount,
                        },
                    )
                ],
            }
        )

    def action_view_order(self):
        print("...............Button clicked...........")
        record_id = self.env["sale.order"].search([("name", "=", self.name)])
        print("record id : ", record_id)
        self.ensure_one()
        return {
            "type": "ir.actions.act_window",
            "name": "sale order",
            "res_model": "sale.order",
            "view_mode": "form",
            "view_id": self.env.ref("sale.view_order_form").id,
            "res_id": record_id.id,
            "target": "current",
        }


class SaleOrderOption(models.Model):
    _inherit = "sale.order"

    order_history_ids = fields.One2many("sh.invers", "custom_field_id")

    # def create(self, val_list):
    #     res = super().create(val_list)
    #     super(SaleOrderOption, self)._compute_order_history()
    #     return res

    @api.onchange("partner_id")
    def _compute_order_history(self):
        counter = 1

        order_setting_value = self.env.company.last_no_order
        days_settings_value = self.env.company.last_no_days
        end_date = datetime.now()
        start_date = end_date - timedelta(days=days_settings_value)
        stages = self.env.company.stages
        stage_list = []
        for stage in stages:
            if stage.name == "Quotation":
                stage_list.append("draft")
            if stage.name == "Quotation Sent":
                stage_list.append("sent")
            if stage.name == "Sales Order":
                stage_list.append("sale")
            if stage.name == "Cancelled":
                stage_list.append("cancel")

        print("orders : ", order_setting_value)
        print("days  : ", days_settings_value)
        print("stages : ", self.env.company.stages)

        for order in self:
            if order.partner_id:
                domain = [("order_partner_id", "=", order.partner_id.id)]

                line_ids = self.env["sale.order.line"].search(domain)
                print("\n\n\n\nline_ids", line_ids)
                invers_records = []

                for line in line_ids:
                    print("\n\n\norder", line.order_id)
                    print("date : ", line.order_id.date_order.date())
                    print("start_date : ", start_date.date())
                    print("end_date : ", end_date.date())

                    if ((start_date.date() <= line.order_id.date_order.date() <= end_date.date())):
                        print("start date : ", start_date)
                        print("end date : ", end_date)
                        print("order date: ", line.order_id.date_order)
                        if line.state in stage_list:
                            if counter <= order_setting_value:
                                print("stage list : ", stage_list)

                                invers_records.append(
                                    Command.create(
                                        {
                                            "name": line.order_id.name,
                                            "date": line.order_id.date_order,
                                            "product": line.product_id.name,
                                            "price": line.price_unit,
                                            "quantity": line.product_uom_qty,
                                            "unit": line.product_uom.name,
                                            "subtotal": line.price_total,
                                            "status": line.state,
                                            "custom_field_id": order.id,
                                        }
                                    )
                                )
                                counter += 1
                order.order_history_ids = invers_records or False
            else:
                order.order_history_ids = False
