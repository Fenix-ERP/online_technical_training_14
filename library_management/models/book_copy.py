# -*- coding: utf-8 -*-

from odoo import models, fields, api
from odoo.exceptions import ValidationError

class Book(models.Model):
    _name = "library.book.copy"
    _inherits = {"library.book":"book_id"} 
    _description = "Book model copy for library management"
    
    ref_unique = fields.Char("Unique", required=True)
    
    book_id = fields.Many2one("library.book", string="Book",auto_join=True, index=True, ondelete="cascade", required=True)
    
   
    
   