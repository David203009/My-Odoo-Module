from odoo import models, fields

class Project(models.Model):
    _name = 'project_manager.project'
    _description = 'Project Manager Project'

    name = fields.Char(string='Nombre', required=True)
    description = fields.Text(string='Descripción')
    start_date = fields.Date(string='Fecha de Inicio')
    end_date = fields.Date(string='Fecha de Fin')
    task_ids = fields.One2many('project_manager.task', 'project_id', string='Tareas')
