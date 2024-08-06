from  odoo import fields,models

class TopicWizard(models.TransientModel):
    _name="sh.topic.wizard"
    _description="It shows topic of particuler subject"

    topic_name=fields.Char(string="Enter Topic Name: ")
    topic_description=fields.Text(string="Enter Description: ")

    def ButtonObject(self):
        print(self)
        print(f"..............topic name : {self.topic_name}")
        print(">...............................hi")

    def DEF(self):
        print("...............Button clicked...........")
        # print(self.)
        return {
            'type': 'ir.actions.act_window',
            'name': 'sh_topic_semi_wizard_action',
            'res_model': 'sh.semiwizard',
            'view_mode': 'tree',
        
            'target': 'new',
        }
       

