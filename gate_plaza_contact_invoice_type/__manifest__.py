# -*- coding: utf-8 -*-
{
    'name': "gate_plaza_contact_invoice_type",

    'summary': """
        Choose Contact Invoicing Type
    """,

    'description': """
        Choose Contact Invoicing Type and Add Fields To Invoices
    """,

    'author': "Roaya",
    'website': "https://www.roayadm.com",

    'license': 'OPL-1',
    'version': '16.0',

    'depends': ['account'],

    'data': [
        'views/res_partner.xml',
        'views/account_move.xml',
    ],
}
