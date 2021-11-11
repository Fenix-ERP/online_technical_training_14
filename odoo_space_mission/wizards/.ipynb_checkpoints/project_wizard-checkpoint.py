# -*- coding: utf-8 -*-

from odoo import models, fields, api

class Mission(models.TransientModel):
    _name = "space.project.wizard"
    _description = "Space Project Wizard"
    
    def _default_mission_id(self):
        return self.env['space.mission'].browse(self._context.get('active_id')).id
    
    name = fields.Char("Name")
    description = fields.Text("Description")
    mission_id = fields.Integer('Mission', default=_default_mission_id)
    
    
    def action_create_project(self):
        for record in self:
            project_obj = self.env['project.project']
            project = {
                'name': record.name,
                'description': record.description,
                'mission_id': record.mission_id
            }
            
            project_obj.create(project)