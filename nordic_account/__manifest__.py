# -*- coding: utf-8 -*-

{
    'name': 'Nordic Account',
    'version': '14.0.1.0.0',
    'category': 'Generic Modules/Account',
    'summary': """

    """,
    'description': """ """,
    'author': 'Applet Solutions',
    'company': 'Applet Solutions',
    'website': 'https://www.appletsolution.tech',
    'depends': ['account',],
    'data': [
        'views/account_move_views.xml',
        'views/invoice_report_template.xml',
        'views/res_config_settings_view.xml',
        'reports/invoice_report.xml',
        'security/ir.model.access.csv',

    ],
    'installable': True,
    'auto_install': False,
    'application': False,
    'license': 'AGPL-3',
}