# -*- coding: utf-8 -*-

from odoo import models, fields, api

from odoo.exceptions import UserError

class Rental(models.Model):
    _name = "library.rental"
    _description = "Odoo's library rental model"
    
    name = fields.Char("Rental Name")
    book_id = fields.Many2one(comodel_name='library.book', string='Books', required=True)
#     customer = fields.Many2many("res.partner", "library_customer", string="Customers", required=True)
    customer = fields.Many2one("res.partner", string="Customers", required=True)
    