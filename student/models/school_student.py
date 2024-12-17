from odoo import api, fields, models, _
from odoo.exceptions import UserError


class SchoolStudent(models.Model):
    _name = 'school.student'
    _description = 'School Student Information'

    name = fields.Char(string='Student Name')
    school_id = fields.Many2one('school.profile', string='School')
    hobby_list = fields.Many2many('student.hobby', 'school_hobby_rel', 'student_id', 'hobby_id', string='Hobbies')
    is_virtual_class = fields.Boolean(related='school_id.offline_class', string='Is Virtual Class')
    school_address = fields.Text(string='School Address', related='school_id.address')
    currency_id = fields.Many2one('res.currency', string='Currency Type')
    student_fees = fields.Monetary(string='Fees For Student',currency_field='currency_id')
    # ref_id = fields.Reference([('school.profile'),
    #                            ('account.move','Invoice')]
    #                           , string='Fees Reference')
    ref_id = fields.Reference(
        [('school.profile', 'school.profile'),
         ('account.move', 'account.move')],
        string='Fees Reference'
    )
    # add archived and unarchived
    active = fields.Boolean('Active', default=True)

    def write(self, values):
        result = super(SchoolStudent, self).write(values)
        for record in self:
            if not record.hobby_list:
                raise UserError(_('Please select at least one hobby'))
        return result

    # override copy orm method
    def copy(self, default=None):
        if default is None:
            default = {}
        if 'name' not in default:
            default['name'] = _("%s (copy)") % (self.name)
        return super(SchoolStudent, self).copy(default)

    def unlink(self):
        for rec in self:
            if rec.student_fees != 0:
                raise UserError(_('You cannot delete this %s student profile'%rec.name))
        res = super(SchoolStudent, self).unlink()
        return res


class SchoolProfile(models.Model):
    _inherit = 'school.profile'

    school_list = fields.One2many('school.student', 'school_id', string='School List', )

    # override create method
    @api.model
    def create(self, vals):
        rtn = super(SchoolProfile, self).create(vals)
        if not rtn.school_list:
            raise UserError(_('Student list is empty!'))
        return rtn
