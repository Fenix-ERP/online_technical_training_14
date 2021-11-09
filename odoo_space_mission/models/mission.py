# -*- coding: utf-8 -*-

from odoo import models, fields, api

from odoo.exceptions import UserError

class Mission(models.Model):
    _name = "space.mission"
    _description = "Odoo's mission model"
    
    name = fields.Char("Name", related="spaceship_id.name", readonly=True)
    spaceship_id = fields.Many2one(comodel_name='space.spaceship', string='Assigned Spaceship', required=True)
    crew_members = fields.Many2many("res.partner", "space_crew_contacts", string="Crew Members", required=True)
    launch_date = fields.Date('Launch Date', required=True)
    return_date = fields.Date('Return Date')
    