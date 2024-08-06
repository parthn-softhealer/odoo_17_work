{
    'name': 'sh_college',
    'version': '1.2',
    'category': 'course',
    'summary': 'sh_college',
    'description': "This module contains all the common features of Sales Management and eCommerce.",
    'depends': [
        'base'  ,'sale' ],
    'data': [
        # views 
        'security/ir.model.access.csv',     
        'views/sh_person_view.xml',
        'views/sh_checking_view.xml',
        'reports/person_report_view.xml',
    ],
  
    'installable': True,
    'application': True, 
}
