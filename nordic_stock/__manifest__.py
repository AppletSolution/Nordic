# -*- coding: utf-8 -*-

{
    'name': 'Nordic Inventory',
    'version': '14.0.1.0.0',
    'category': 'Generic Modules/Inventory',
    'summary': """

    """,
    'description': """ """,
    'author': 'Applet Solutions',
    'company': 'Applet Solutions',
    'website': 'https://www.appletsolution.tech',
    'depends': ['product','stock','purchase'],
    'data': [
        'data/uom_data.xml',
        'views/stock_views.xml',
        'views/purchase_view.xml',
        'report/report_nordic_picking.xml',
        'report/stock_report_view.xml',

    ],
    'installable': True,
    'auto_install': False,
    'application': False,
    'license': 'AGPL-3',
}