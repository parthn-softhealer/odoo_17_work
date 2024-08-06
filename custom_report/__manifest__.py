{
    'name': 'custom_report',
    'version': '1.2',
    'category': '',
    'summary': 'custom_report',
    'description': "This module is custom_report",
    'depends': [
        'base' , 'sale'
    ],
    'data': [
        'security/ir.model.access.csv',
        'wizard/wizard_view.xml',
        
        'reports/report.xml' ,
        'views/temp.xml'   
    ],
    'installable': True,
    'application': True, 

}