from odoo import models, fields
from odoo import fields, models


class ShCompany(models.Model):
    _inherit = "res.company"
    last_no_order = fields.Integer(string="Last No of Order")
    last_no_days = fields.Integer(string="Last No of day's order")
    reorder = fields.Boolean(string="Reorder")
    stages = fields.Many2many("selection.stage", string="Stages")


class ShSettings(models.TransientModel):
    _inherit = "res.config.settings"

    last_no_order = fields.Integer(
        related="company_id.last_no_order", string="Last No of Order", readonly=False
    )
    last_no_days = fields.Integer(
        related="company_id.last_no_days",
        string="Last No of day's order",
        readonly=False,
    )
    reorder = fields.Boolean(
        related="company_id.reorder", string="Reorder", readonly=False
    )
    stages = fields.Many2many(
        "selection.stage", related='company_id.stages', readonly=False)


class Stage(models.Model):
    _name = 'selection.stage'
    _description = 'Selection Stage'

    name = fields.Char(string="Stage", required=True)
