from odoo import models, fields

class Task(models.Model):
    _inherit = 'project_manager.task'

    state = fields.Selection([
        ('do', 'Hacer'),
        ('in_progress', 'En Progreso'),
        ('done', 'Hecho'),
    ], string='Estado', default='do', group_expand='_read_group_state_ids')

    def _read_group_state_ids(self, states, domain, order):
        return ['do', 'in_progress', 'done']
