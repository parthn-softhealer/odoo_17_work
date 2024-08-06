from odoo import fields , models 

class ShProductWizard(models.TransientModel) :
    _name = "sh.product.wizard"
    # _inherits = {'product.product': 'product_tmpl_id'}

    product_tmpl_id = fields.Many2one('product.product', required=True,string="Product Template")
    
    

    def update_sale_order_line_record(self) :

        print("\n\n---------------------")
        print("self : " , self.env.context )
        record = self.env[self.env.context['active_model']].browse(self.env.context['active_id'])
        
        if record : 
            print("record :" , record)
            print("record id : " , record.id)
            print("data : " , record.product_template_id, self.product_tmpl_id )        
            record.product_id= self.product_tmpl_id

        print("----------after-----------\n\n",record.product_uom_qty)

