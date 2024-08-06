from odoo import fields,models,api

class ShMix(models.Model):
    _name="sh.mix"
    _description="merger two fields"

    name=fields.Char(string=" first name",default=" ",required=True)
    lastname=fields.Char(string="last name",default=" ",required=True)
    mix=fields.Char(string="Full name" ,default=" ")

    @api.onchange('name','lastname')
    def _onchange_(self):
        self.mix=str(self.name)+str(self.lastname)
        print(f'\n\n\n>>> 14 | {self.mix}:  ')
            


    # @api.model_create_multi
    # def create(self, vals_list):
    #     print(".........",vals_list[0])
        
    #     vals_list[0]['mix']=vals_list[0]['name']+vals_list[0]['lastname']
       
        
    #     print("..............",vals_list[0]['mix'])   
    #     lines = super().create(vals_list)
    #     return lines
    
   
    
    
    # def write(self, values):
    #     for record in self:
    #         new_name = values.get('name', record.name)
    #         new_lastname = values.get('lastname', record.lastname)
    #         new_mix = new_name + new_lastname

    #         if record.mix != new_mix:
    #             values['mix'] = new_mix
    
    #     result = super().write(values)
    #     return result
        
    

