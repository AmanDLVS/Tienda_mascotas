# -*- coding: utf-8 -*-
{
    'name': "MemePet",

    'summary': """
         Módulo para la gestión de una tienda de mascotas""",

    'description': """
        Es un modulo adaptado para la gestion de una tienda de mascotas, con gestion de dependientes,mascotas,especies,ventas,clientes,etc...
    """,

    'author': "AmanDLVS",
    'website': "https://github.com/AmanDLVS",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/15.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Industria',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base'],

    # always loaded
    'data': [
        "security/security.xml",
        'security/ir.model.access.csv',
        'data/data.xml',
        'views/views.xml',
        'views/templates.xml',
        'reports/reports.xml'
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}
