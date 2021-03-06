{
    "name": "Auto Generate Lot Number in Manufacturing",
    "version": "11.0.2.12",
    "category": "Manufacturing",
    "summary": """
	Auto generate Lot no in Manufacturing when we have Produce Manufacturing Order lot no generate based on production Date/Today Date.
	""",
    "author": 'Vraja Technologies',
    'price': 11,
    'currency': 'EUR',
    "depends": ['mrp','stock'],
    "data": [
        'wizard/res_config.xml',
    ],
    'qweb': [],
    'css': [],
    'js': [],
    'images': [
        'static/description/auto_generate_mo.png',
    ],
    'demo': [],
    'installable': True,
    'auto_install': False,
    'application': True,
    'license': 'LGPL-3',
}
