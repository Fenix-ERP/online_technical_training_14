# -*- coding: utf-8 -*-

from odoo import models, fields, api

from odoo.exceptions import UserError

class Project(models.Model):
    _inherit = "project.project"
    
    mission_id = fields.Many2one('space.mission', string='Mission')
    
    def mission_form_view(self):
        action = self.env['ir.actions.act_window']._for_xml_id('odoo_space_mission.space_mission_window')
        action['domain'] = [('id', 'in', self.mission_id.ids)]
        
        return action
    