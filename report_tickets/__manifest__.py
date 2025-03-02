# report_tickets/__manifest__.py
{
    'name': 'Report Tickets Module',
    'version': '1.0',
    'summary': 'Módulo para agregar un submenú de reportes vacío',
    'description': 'Este módulo añade un submenú vacío bajo el menú de Reporting.',
    'author': 'Tu Nombre',
    'website': 'https://tusitio.com',
    'category': 'Uncategorized',
    'depends': ['helpdesk'],
    'data': [
        'views/ticket_report_menu.xml',
    ],
    'installable': True,
    'application': True,
    'license': 'LGPL-3',
}