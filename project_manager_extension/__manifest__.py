# report_tickets/__manifest__.py
{
    'name': 'Project Manager Extension',
    'version': '1.0',
    'summary': 'Extension para el módulo de Project Manager',
    'description': 'Añade funcionalidades adicionales al módulo de Project Manager',
    'author': 'Tu Nombre',
    'website': 'https://tusitio.com',
    'category': 'Uncategorized',
    'depends': ['project_manager'],
    'data': [
        'security/ir.model.access.csv',
        'views/project_view.xml',
        'views/project_stage_views.xml',
        'views/menu.xml',
    ],
    'installable': True,
    'application': True,
    'license': 'LGPL-3',
}