from odoo import api, fields, models

class StudentHobby(models.Model):
    _name = 'student.hobby'
    _description = 'Student Hobbies'

    name = fields.Char(string='Hobbies')
