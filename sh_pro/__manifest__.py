{
    'name': 'sh_pro',
    'version': '1.2',
    'category': 'course',
    'summary': 'sh_pro',
    'description': "This module contains all the common features of Sales Management and eCommerce.",
    'depends': [
        'base'
    ],
    'data': [
        # views 
        'security/ir.model.access.csv',
        'views/sh_res_partner_view.xml',
        'views/sh_product_product_view.xml',
        'views/sh_sale_order_view.xml',
        'views/sh_sale_order_line_view.xml',
        'views/sh_account_tax_view.xml'
    ],
    'installable': True,
    'application': True, 
}
