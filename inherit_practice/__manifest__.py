{
    'name': 'inherit_practice',
    'version': '1.2',
    'category': '',
    'summary': 'inherit_practice',
    'description': "This module is inherit_practice",
    'depends': [
        'base' , 'sale'
    ],
    'data': [
        'wizard/select_product_view.xml',
        'security/ir.model.access.csv',

        # 'views/sale_order_inherit_view.xml',
        'views/sh_school_student_view.xml',
        'views/product_inherit_view.xml',
        'views/order_line_inherit_view.xml',
    ],
    'installable': True,
    'application': True, 

}