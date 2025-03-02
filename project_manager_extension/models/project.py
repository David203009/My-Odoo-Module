from odoo import models, fields

class Project(models.Model):
    _inherit = 'project_manager.project'

    stage_id = fields.Many2one('project_manager.project_stage', 'Etapa', group_expand='_read_group_stage_ids',)

    def _read_group_stage_ids(self, stages, domain, order):
        return self.env['project_manager.project_stage'].search([])
