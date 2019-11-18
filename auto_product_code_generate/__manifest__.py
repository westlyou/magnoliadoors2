# -*- coding: utf-8 -*-
# Part of Odoo. See COPYRIGHT & LICENSE files for full copyright and licensing details.

{
    'name': 'Auto assigned Product SKU',
    'version' : '1.1',
    'summary': 'Auto assigned Product SKU/Internal Reference',
    'sequence': 30,
    'description': """
    Auto assigned Product SKU/Internal Reference.
    """,
    'category': 'Sales',
    'author': 'Synconics Technologies Pvt. Ltd.',
    'website': 'www.synconics.com',
    'depends': ['sale_management'],
    'data': [
        'views/res_config_settings_view.xml',
        'wizard/multi_product_internal_reference_view.xml',
    ],
    'demo': [

    ],
    'images': [
        'static/description/main_screen.jpg'
    ],
    'price': 35.0,
    'currency': 'EUR',
    'installable': True,
    'application': True,
    'auto_install': False,
    'license': 'OPL-1',
}

# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4: