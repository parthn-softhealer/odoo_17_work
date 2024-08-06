import os


def create_file(path, content=""):
    with open(path, "w") as file:
        file.write(content)


def create_odoo_module_structure(module_name):

    structure = [
        os.path.join(module_name, "models", "__init__.py"),
        os.path.join(module_name, "models", "sh_model.py"),
        os.path.join(module_name, "views", "temp.xml"),
        os.path.join(module_name, "security", "ir.model.access.csv"),
        os.path.join(module_name, "__init__.py"),
        os.path.join(module_name, "__manifest__.py"),
    ]

    # Create directories and files
    for file_path in structure:
        os.makedirs(os.path.dirname(file_path), exist_ok=True)
        create_file(file_path)

    # --------------------CSV----------------------------
    temp_csv_path = os.path.join(module_name, "security", "ir.model.access.csv")
    temp_csv_content = (
        "id,name,model_id:id,group_id:id,perm_read,perm_write,perm_create,perm_unlink\n"
    )
    create_file(temp_csv_path, temp_csv_content.strip())
    # ------------------------------------------------

    # ---------------------XML---------------------------
    temp_xml_path = os.path.join(module_name, "views", "temp.xml")
    temp_xml_content = """
<odoo>
    <record id="view_form" model="ir.ui.view">
        <field name="name">view.form</field>
        <field name="model">sh.</field>
        <field name="arch" type="xml">
            <form string="">
                <sheet>
                    <group>
                        <field name="" string=""/>
                    </group>
                </sheet>
            </form>
        </field>
    </record>
    
    <record id="view_tree" model="ir.ui.view">
        <field name="name">view.tree</field>
        <field name="model">sh.</field>
        <field name="arch" type="xml">
            <tree string="">
                <field name="" string=""/>
            </tree>
        </field>
    </record>

    <record id="_action" model="ir.actions.act_window">
        <field name="name"></field>
        <field name="res_model">sh.</field>
        <field name="view_mode">tree,form</field>
    </record>

    <menuitem
        id=""
        name=""
        action="_action"
    />
</odoo>
"""
    create_file(temp_xml_path, temp_xml_content.strip())
    # ------------------------------------------------

    # -------------------Manifest--------------------------
    temp_manifest_path = os.path.join(module_name, "__manifest__.py")
    temp_manifest_content = (
        """
{"""
        + f"""
    'name': '{module_name}',
    'version': '1.2',
    'category': '',
    'summary': '{module_name}',
    'description': "This module is {module_name}",
    'depends': [
        'base'
    ],
    'data': [
        # views 
        #'views/',
        'security/ir.model.access.csv'     
    ],
    'installable': True,
    'application': True, 
"""
        + """
}
"""
    )
    create_file(temp_manifest_path, temp_manifest_content.strip())
    # ------------------------------------------------

    # -------------------only 1st Model-----------------------------
    temp_model_path = os.path.join(module_name, "models", "sh_model.py")
    temp_model_content = """
from odoo import models , fields

class Sh(models.Model):
    _name = "sh."
    
    temp = fields.Char(string = "")
    
"""
    create_file(temp_model_path, temp_model_content.strip())
    # ------------------------------------------------

    # -------------------outer : __init__ --------------------------
    temp_init_path = os.path.join(module_name, "__init__.py")
    temp_init_content = """
from . import models    
"""
    create_file(temp_init_path, temp_init_content.strip())
    # ------------------------------------------------

    print(f"Module structure for '{module_name}' created successfully.")


# Specify the name of the module
module_name = "crm_opp"

# Create the Odoo module structure
create_odoo_module_structure(module_name)


# from datetime import datetime, timedelta

# def get_last_n_days(n):
#     current_date = datetime.now()
#     start_date = current_date - timedelta(days=n)
#     return start_date, current_date

# # Example usage
# start_date, end_date = get_last_n_days(5)
# print(f"Start Date: {start_date}")
# print(f"End Date: {end_date}")
