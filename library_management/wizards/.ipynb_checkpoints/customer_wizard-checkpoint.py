# -*- coding: utf-8 -*-

from odoo import models, fields, api

class Customer(models.TransientModel):
    _name = "library.customer.wizard"
    _description = "Selected book Wizard"
    
    customers = fields.Many2one("res.partner", string="Customers", required=True)
#     rental = fields.One2many("library.rental", "Rentals")
            
            
   