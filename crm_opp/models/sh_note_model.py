from odoo import models
from odoo.tools import html2plaintext


class ShNoteModel(models.Model):
    _inherit = 'product.template'

    def _transfer_note_(self):
        for rec in self:
            rec.description_sale = html2plaintext(rec.description)