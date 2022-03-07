{
    'name': 'BDTA',
    'version': '14.0',
    'summary': 'BDTA',
    'sequence': -100,
    'description': """BDTA""",
    'category': 'Productivity',
    'website': 'https://www.odoo.com/page/billing',
    'license': 'LGPL-3',
    'images': [],
    'depends': [
        'mail',
        'report_xlsx',
    ],
    'data': [
        'data/data.xml',
        'security/ir.model.access.csv',
        'views/appointment_view.xml',
        'views/report_appointment_view.xml',
        'views/res_partner_view.xml',
        'views/menu_view.xml',
        'report/report_xlsx.xml',
        'report/xlsx_report.xml',
        'wizard/appointment_report_winzard.xml',
        'wizard/res_partner_report_winzard.xml',
    ],
    'demo': [],
    'qweb': [],
    'installable': True,
    'application': True,
    'auto_install': False
}
