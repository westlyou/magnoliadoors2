# -*- coding: utf-8 -*-
{
    'name': "Door_custom_measure",

    'summary': """
        Medir puertas custom""",

    'description': """
        Long description of module's purpose
    """,

    'author': "My Company",
    'website': "http://www.yourcompany.com",

    # Categories can be used to filter modules in modules listsing
    # Check https://github.com/odoo/odoo/blob/master/odoo/addons/base/module/module_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base','purchase','sale'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
      
	
	'views/purchase_order_line_xmarts.xml',
	'views/sale_order_line_xmarts.xml',
	'reports/reporte.xml',
	'reports/reportes.xml',

	
	
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
	
    "installable": True,
    "application": True,
    "auto_install": True,
}
