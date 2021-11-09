# -*- coding: utf-8 -*-

from odoo import models, fields, api

class Task(models.Model):
    _name = "volunteers.task"
    _description = "Task model to split the work"
    
    name = fields.Char("Name", required=True)
    datetime_start = fields.Datetime(string="Start Task")
    datetime_stop = fields.Datetime(string="Stop Task")
    repeat = fields.Boolean(string="Repeats")
    frequency = fields.Char(string="frequency:")
    task_type = fields.Selection(
        string="Task Type",
        selection=[
            ('sales', 'Sales'),
            ('customer', 'Customer Service'),
            ('usher', 'Usher'),
            ('lunch', 'Lunch Time'),
        ],
        copy=False
    )
    volunteer_ids = fields.Many2many("res.partner", string="Volunteers", required=True)