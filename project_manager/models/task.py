from odoo import models, fields

class Task(models.Model):
    _name = 'project_manager.task'
    _description = 'Project Manager Task'

    name = fields.Char(string='Nombre', required=True)
    description = fields.Text(string='Descripción')
    start_date = fields.Date(string='Fecha de Inicio')
    end_date = fields.Date(string='Fecha de Fin')
    state = fields.Selection([
        ('do', 'Hacer'),
        ('in_progress', 'En Progreso'),
        ('done', 'Hecho'),
    ], string='Estado', default='do')
    project_id = fields.Many2one('project_manager.project', string='Proyecto')
    user_id = fields.Many2one('res.users', string='Responsable')
