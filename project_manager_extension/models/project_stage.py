from odoo import models, fields

class ProjectStage(models.Model):
    _name = 'project_manager.project_stage'
    _description = 'Project Stage'
    _order = 'sequence, name'

    name = fields.Char('Name', required=True)
    sequence = fields.Integer('Sequence', default=10)
    description = fields.Text('Description')
