from odoo import models, fields, api

class OperatorTask(models.Model):
    _name = 'operator.task'
    _description = 'Operator Task'
    _order = 'create_date desc'

    order_number = fields.Char(string='Номер заказа', required=True)
    order_name = fields.Char(string='Название заказа')
    details = fields.Text(string='Подробности')
    
    state = fields.Selection([
        ('ready', 'Готово к работе'),
        ('in_progress', 'В работе'),
        ('done', 'Выполнено'),
        ('reject', 'Брак')
    ], string='Статус', default='ready')
    
    start_time = fields.Datetime(string='Принят')
    end_time = fields.Datetime(string='Завершен')
    
    operator_id = fields.Many2one('res.users', string='Оператор')

    def action_start_work(self):
        for task in self:
            task.write({
                'state': 'in_progress',
                'start_time': fields.Datetime.now(),
                'operator_id': self.env.user.id
            })

    def action_complete(self):
        for task in self:
            task.write({
                'state': 'done',
                'end_time': fields.Datetime.now()
            })

    def action_reject(self):
        for task in self:
            task.write({
                'state': 'reject',
                'end_time': fields.Datetime.now()
            })