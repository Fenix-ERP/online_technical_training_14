# -*- coding: utf-8 -*-

{
    "name": "Odoo Space Mission",
    "summary": "In order for Odoo to get to the moon, they need a rocket.",
    "version": "14.0.1.0.0",
    "author": "Joseph Armas",
    "category": "Training",
    "website": "",
    "depends": ["base", "contacts", "project"],
    "data": [
        "security/space_groups.xml",
        "security/ir.model.access.csv",
        "views/space_menuitems.xml",
        "views/spaceship_views.xml",
        "views/mission_views.xml",
        "views/project_views.xml",
    ],
    "demo": [
        "demo/space_mission_demo.xml"
    ],
}
