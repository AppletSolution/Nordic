# -*- coding: utf-8 -*-

{
    'name': 'Nordic Sales',
    'version': '14.0.1.0.0',
    'category': 'Generic Modules/Sales',
    'summary': """
       
    """,
    'description': """ """,
    'author': 'Applet Solutions',
    'company': 'Applet Solutions',
    'website': 'https://www.appletsolution.tech',
    'depends': ['sale','sale_management'],
    'data': [
        'views/sale_order_view.xml',
        'report/sale_order_template.xml',
        'security/ir.model.access.csv',
        'data/mail_activity_data.xml',
    ],
    'installable': True,
    'auto_install': False,
    'application': False,
    'license': 'AGPL-3',
}