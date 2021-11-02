# -*- coding: utf-8 -*-

from odoo import models, fields, api

class Task(models.Model):
    _name = "volunteers.task"
    _description = "Task model to split the work"
    
    name = fields.Char("Name", required=True)
    date_start = fields.Date(string="Start Task")
    date_stop = fields.Date(string="Stop Task")
    repeat = fields.Boolean(string="Repeats")
    frequency = fields.Char(string="frequency:")
    task_type = fields.Selection(
        string="Task Type",
        selection=[
            ('practice', 'Practice'),
            ('theoretical', 'Theoretical')
        ],
        copy=False
    )