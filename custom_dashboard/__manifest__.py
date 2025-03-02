# report_tickets/__manifest__.py
{
    'name': 'Custom Dashboard',
    'version': '1.0',
    'summary': 'Un dashboard personalizado usando qweb y owl',
    'description': 'Un dashboard personalizado usando qweb y owl',
    'author': 'Tu Nombre',
    'website': 'https://tusitio.com',
    'category': 'Uncategorized',
    'depends': ['web', 'project_manager'],
    'data': [
        'security/ir.model.access.csv',

        'views/dashboard_views.xml',
        'views/menu.xml',
    ],
    'assets': {
    'web.assets_backend': [
        'custom_dashboard/static/src/js/dashboard.js',
        'custom_dashboard/static/src/xml/dashboard.xml',
    ],
},
    'installable': True,
    'application': True,
    'license': 'LGPL-3',
}