# -*- coding: utf-8 -*-

from odoo import models, fields, api

from odoo.exceptions import UserError

class Spaceship(models.Model):
    _name = "space.spaceship"
    _description = "Odoo's spaceship model"
    
    name = fields.Char("Name", required=True)
    length = fields.Float("Length", required=True, default=0)
    width = fields.Float("Width", required=True, default=0)
    dimension = fields.Float("Dimension", compute="_compute_dimension", readonly=True)
    fuel_type = fields.Selection(
        string="Fuel Type",
        selection=[
            ('liquid', 'Liquid'),
            ('solid', 'Solid'),
            ('hydrogen', 'Liquid Hydrogen')
        ],
        copy=False
    )
    ship_type = fields.Selection(
        string="Ship Type",
        selection=[
            ('flyby', 'Flyby spacecraft'),
            ('orbiter', 'Orbiter spacecraft'),
            ('lander', 'Lander spacecraft')
        ],
        copy=False
    )
    passengers_number = fields.Integer("Number of passengers")
    active = fields.Boolean("Active", default=True)
    
    @api.depends('length','width')
    def _compute_dimension(self):
        for record in self:
            dimension = record.length * record.width
            record.write({'dimension': dimension})
            
    @api.constrains('length','width')
    def _constrain_dimension(self):
        for record in self:
            if record.width > record.length:
                raise UserError("The width of the spaceship can't be bigger than the length")