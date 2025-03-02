from odoo import models, fields

class Dashboard(models.Model):
    _name = 'custom_dashboard.dashboard'
    _description = 'Custom Dashboard'

    name = fields.Char(string='Name', required=True)
    description = fields.Text(string='Description')
