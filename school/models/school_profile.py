from odoo import api, fields, models


class SchoolProfile(models.Model):
    _name = 'school.profile'

    name = fields.Char(string='Name', help='This is a School Name', default='First School')
    email = fields.Char(string='Email', default='xyz@gmail.com')
    phone = fields.Char(string='Phone', default='1234567890')
    offline_class = fields.Boolean(string='Offline Class')
    school_rank = fields.Integer(string='School Rank', compute='compute_school_rank')
    result = fields.Float(string='Result', digits=(2, 3))
    address = fields.Text(string='Address', default='Dhaka,Mirpur12')
    establish_date = fields.Date(string='Establish Date', default=fields.Date.today)
    open_date = fields.Datetime(string='Open Date', default=fields.Datetime.now)
    school_type = fields.Selection([
        ('public', 'Public School'),
        ('private', 'Private School'),
        ('international', 'International School'),
        ('charter', 'Charter School'),
        ('online', 'Online School'),
        ('boarding', 'Boarding School'),
        ('montessori', 'Montessori School'),
    ], string='School Type', default='private')
    documents = fields.Binary(string='Documents')
    document_name = fields.Char(string='File Name')
    school_description = fields.Html(string='School Description')
    school_image = fields.Binary(string='Upload school Image', max_width=100, max_height=100)



    # @api.onchange('fields name')
    @api.onchange('school_type')
    def compute_school_rank(self):
        for rec in self:
            if rec.school_type == 'public':
                rec.school_rank = 100
            elif rec.school_type == 'private':
                rec.school_rank = 50
            elif rec.school_type == 'international':
                rec.school_rank = 40
            elif rec.school_type == 'charter':
                rec.school_rank = 30
            elif rec.school_type == 'online':
                rec.school_rank = 20
            elif rec.school_type == 'boarding':
                rec.school_rank = 10
            elif rec.school_type == 'montessori':
                rec.school_rank = 70
            else:
                rec.school_rank = 0
