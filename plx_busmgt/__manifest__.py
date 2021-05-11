# -*- coding: utf-8 -*-
{
    'name': "Bus Management",

    'summary': """
        Bus Management Software""",

    'description': """
        Bus Management Software
    """,

    'author': "Plexada SI",
    'website': "http://www.plexada-si.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/13.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Productivity',
    'version': '1.0',

    # any module necessary for this one to work correctly
    'depends': ['base', 'fleet', 'stock', 'product', 'project'],

    # always loaded
    'data': [],
    # only loaded in demonstration mode
    'demo': [],
    'installable': True,
    'application': True,
    'auto_install': False,
}
