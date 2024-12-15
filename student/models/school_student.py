from odoo import api, fields, models


class SchoolStudent(models.Model):
    _name = 'school.student'
    _description = 'School Student Information'

    name = fields.Char(string='Student Name')
    school_id = fields.Many2one('school.profile', string='School')


class SchoolProfile(models.Model):
    _inherit = 'school.profile'

    school_list = fields.One2many('school.student', 'school_id', string='School List')
