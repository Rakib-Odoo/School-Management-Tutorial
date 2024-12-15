from odoo import api, fields, models

class SchoolProfile(models.Model):
    _name = 'school.profile'

    name = fields.Char(string='Name', help='This is a School Name')
    email = fields.Char(string='Email')
    phone = fields.Char(string='Phone')
    offline_class = fields.Boolean(string='Offline Class')
    school_rank = fields.Integer(string='School Rank')
    result = fields.Float(string='Result', digits=(2,3))
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
    ], string='School Type')
    documents = fields.Binary(string='Documents')
    document_name = fields.Char(string='File Name')
    school_description = fields.Html(string='School Description')
    school_image = fields.Binary(string='Upload school Image',max_width=100, max_height=100)