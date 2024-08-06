{
    'name': 'crm_opp',
    'version': '1.2',
    'category': '',
    'summary': 'crm_opp',
    'description': "This module is crm_opp",
    'depends': [
        'base', 'crm', 'product'
    ],
    'data': [
        # views
        'security/ir.model.access.csv',
        'views/transfer_note.xml',
        'views/crm_seq.xml',
        'views/crm_tree.xml'
    ],
    'installable': True,
    'application': True,

}
