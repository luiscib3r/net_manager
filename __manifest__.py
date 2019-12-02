# -*- coding: utf-8 -*-
{
    'name': "Net Manager",

    'summary': """
        Net Manager """,

    'description': """
    """,

    'author': "Luis Correa (Soft4Cuba)",
    'website': "https://soft4cuba.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/12.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Application',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base'],

    # always loaded
    'data': [
        'security/group.xml',
        'security/ir.model.access.csv',
        'security/rules.xml',
        'views/menu.xml',
        'views/cliente.xml',
        'views/servicio.xml',
        'views/ipaddress.xml',
        'views/pago.xml',
        'views/templates.xml',
        'data/stage.xml',
        'data/cron.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
    'installable': True,
    'application': True,
}
