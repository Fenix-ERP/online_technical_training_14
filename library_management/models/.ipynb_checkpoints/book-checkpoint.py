# -*- coding: utf-8 -*-

from odoo import models, fields, api
from odoo.exceptions import ValidationError

class Book(models.Model):
    _name = "library.book"
    _description = "Book model for library management"
    
    name = fields.Char("Name", required=True)
    authors = fields.Char("Authors", required=True)
    editors = fields.Char("Editors", required=True)
    publisher = fields.Char("Publisher", required=True)
    year_of_edition = fields.Char("Year of Edition")
    isbn = fields.Char("ISBN", required=True)
    genere = fields.Selection([
        ('drama', 'Drama'),
        ('horror', 'Horror'),
        ('comedy', 'Comedy')
    ], "Genere", required=True)
    note = fields.Text("Note")
    
    @api.onchange('isbn')
    def _onchange_length_isbn(self):
        if len(self.isbn) != 13:
            raise ValidationError("The isbn must be 13 characters long")
            
    
    
   