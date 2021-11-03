# -*- coding: utf-8 -*-

from odoo import models, fields, api

class Spaceship(models.Model):
    _name = "space.spaceship"
    _description = "Odoo's spaceship model"
    
    name = fields.Char("Name", required=True)
    dimensions = fields.Float("Dimension", help="Dimension expressed in cubic meters")
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