from odoo import api, fields, models

class SchoolProfile(models.Model):
    _name = 'school.profile'

    name = fields.Char(string='Name', required=True)
    email = fields.Char(string='Email')
    phone = fields.Char(string='Phone')