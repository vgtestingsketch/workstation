{
    'name': 'Workstation',
    'version': '1.0',
    'summary': 'Automated Workplace for Production Operators',
    'author': 'АСАИ Софт',
    'category': 'Manufacturing',
    'depends': ['base'],
    'data': [
        'security/ir.model.access.csv',
        'views/operator_task_views.xml',
    ],
    'installable': True,
    'application': True,
    'licence': 'LGPL-3',
}