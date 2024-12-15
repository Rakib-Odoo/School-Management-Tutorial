{
    'name':'School Student',
    'category': 'School Management System',
    'version': '1.1',
    'description': 'School management system supported in odoo13.',
    'author': 'Rakib Hasan',
    'sequence': 1,
    'depends': ['base','school'],
    'data': [
        'security/ir.model.access.csv',
        'views/menu_view.xml',
        'views/student_view.xml',
    ],
    'installable': True,
    'application': True
}