{
    'name': 'Follow up Report',
    'category': 'account',
    'summary': 'Follow up Report - Email Send',
    'version': '12.0',
     
    'depends': [
        'account_reports',       
    ],

    'data': [
        'views/inherited_res_partner_view.xml',
        'views/followup_report.xml',
    ],
    
    'installable': True,
    'auto_install': False, 
}