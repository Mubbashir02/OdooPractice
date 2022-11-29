
{
    'name' : 'Hospital Managment',
    'version' : '1.1',
    'summary': 'Invoices & Payments',
    'sequence': 15,
    'description': """
Invoicing & Payments
====================
The specific and easy-to-use Invoicing system in Odoo allows you to keep track of your accounting, even when you are not an accountant. It provides an easy way to follow up on your vendors and customers.

You could use this simplified accounting in case you work with an (external) account to keep your books, and you still want to keep track of payments. This module also offers you an easy method of registering payments, without having to encode complete abstracts of account.
    """,
    'category': 'Accounting/Accounting',
    'website': 'https://www.odoo.com/page/billing',
    'images': [],
    'depends': ['mail','sale'],
    'data': [
        'security/ir.model.access.csv',
        'views/patient.xml',
        'views/apoinment.xml',
    ],
    'demo': [
    ],
    'qweb': [
    ],
    'installable': True,
    'application': True,
    'auto_install': False,
    'license': 'LGPL-3',
}
