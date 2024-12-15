from odoo import api, fields, models, _
from odoo.exceptions import UserError


class SchoolStudent(models.Model):
    _name = 'school.student'
    _description = 'School Student Information'

    name = fields.Char(string='Student Name')
    school_id = fields.Many2one('school.profile', string='School')
    hobby_list = fields.Many2many('student.hobby', 'school_hobby_rel', 'student_id', 'hobby_id', string='Hobbies')


class SchoolProfile(models.Model):
    _inherit = 'school.profile'

    school_list = fields.One2many('school.student', 'school_id', string='School List', )

    @api.model
    def create(self, vals):
        rtn = super(SchoolProfile, self).create(vals)
        if not rtn.school_list:
            raise UserError(_('Student list is empty!'))
        return rtn
