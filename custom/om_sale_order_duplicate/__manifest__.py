{
    'name': 'SALE MODEL DUPLICATE',
    'version': '13.0.0.1',
    'category': 'sale',
    'summary': 'sale duplicatiom',
    'description': """
     """,
    "author": "sale",
    'depends': ['sale'],
    'data': [
        'security/ir.model.access.csv',
        'wizard/duplicate_with_wizard.xml',
        'views/sale_order_duplication.xml',
        'views/contact_sales.xml',
    ],
    'license': 'LGPL-3',
    'installable': True,
    'auto_install': False,
    'application': True,
}
