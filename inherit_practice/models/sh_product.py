from odoo import models , fields , api

class ShProduct(models.Model):
    _inherit = "product.template"
    
    my_temp = fields.Char()


    def update_optional_product(self):
        print("\n\n----------------------")
        print("detailed type : " , self.detailed_type)
        consu = self.env['product.template'].search([('detailed_type' , '=' ,self.detailed_type)])
        print("product has type consumable : " , consu)
        self.optional_product_ids = consu
        
        print("----------------------\n\n")

    # @api.create_multi
    # def create(self, val_list) :
