{
    "name": "Auto Generate Lot Number in Incoming Shipment",
    "version": "12.0.11.27",
    "category": "Purchase",
    "summary": """
	Auto generate Lot no in Incoming Shipment when we have confirm Purchase Order based on Schedule date of Incoming Shipment/Today Date.
	""",
    "author": 'EliteInfoTech',
    'price': 8,
    'currency': 'EUR',
    "depends": ['stock','purchase'],
    "data": [
        'wizard/res_config.xml',
    ],
    'qweb': [],
    'css': [],
    'js': [],
    'images': [
        'static/description/auto_generate_lot.png',
    ],
    'demo': [],
    'installable': True,
    'auto_install': False,
    'application': True,
    'license': 'LGPL-3',
}
