# -*- coding: utf-8 -*-

from odoo import models, fields, api

class Book(models.Model):
    _name = "library.book"
    _description = "Book model for library management"
    
    name = fields.Char("Name", required=True)
    authors = fields.Text("Authors", required=True)
    editors = fields.Char("Editors", required=True)
    publisher = fields.Char("Publisher", required=True)
    year_of_edition = fields.Date(string="Year of Edition")
    isbn = fields.Char("ISBN", required=True)
    genere = fields.Selection([
        ('drama', 'Drama'),
        ('horror', 'Horror'),
        ('comedy', 'Comedy')
    ], "Genere", required=True)
    
    
   