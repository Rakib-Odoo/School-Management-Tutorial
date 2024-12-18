{
    'name':'School Student',
    'category': 'School Management System',
    'version': '1.1',
    'description': 'School management system supported in odoo13.',
    'author': 'Rakib Hasan',
    'sequence': 1,
    'depends': ['base','school','web','mail'],
    'data': [
        'security/ir.model.access.csv',
        'data/student_sequence.xml',
        'views/menu_view.xml',
        'views/student_view.xml',
        'views/hobby_view.xml',
        'report/student_report_template.xml',
    ],
    'installable': True,
    'application': True
}