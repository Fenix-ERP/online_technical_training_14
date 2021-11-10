# -*- coding: utf-8 -*-

from odoo import models, fields, api
from datetime import timedelta

import math

from odoo.exceptions import UserError

class Mission(models.Model):
    _name = "space.mission"
    _description = "Odoo's mission model"
    
    name = fields.Char("Name", related="spaceship_id.name", readonly=True, store=True)
    spaceship_id = fields.Many2one(comodel_name='space.spaceship', string='Assigned Spaceship', required=True)
    crew_members = fields.Many2many("res.partner", "space_crew_contacts", string="Crew Members", required=True)
    launch_date = fields.Date('Launch Date', required=True)
    return_date = fields.Date('Return Date')
    fuel_amount = fields.Float("Fuel Amount", compute="_compute_fuel_amount", inverse="_inverse_fuel_amount", store=True)
    engines_number = fields.Integer("Number of Engines", required=True, default=1)
    safety_features = fields.Text("Safety Features")
    
    project_ids = fields.One2many("project.project", "mission_id", "Projects", required=True)
    
    @api.depends('launch_date','return_date','engines_number')
    def _compute_fuel_amount(self):
        for record in self:
            if record.launch_date and record.return_date and record.engines_number:
                days = (record.return_date - record.launch_date).days
                record.fuel_amount = days * record.engines_number * 50
    
    def _inverse_fuel_amount(self):
        for record in self:
            if record.fuel_amount and record.engines_number and record.launch_date:
                days = record.fuel_amount / record.engines_number / 50
                days_delta = math.floor(days)
                record.return_date = record.launch_date + timedelta(days=days_delta)