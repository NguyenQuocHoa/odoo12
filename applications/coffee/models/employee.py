from odoo import models, fields, api, _


class CoffeeEmployee(models.Model):
    _name = 'coffee.employee'
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _description = 'Employee Record'
    _rec_name = 'employee_name'

    @api.depends('employee_age')
    def set_age_group(self):
        if self.employee_age:
            if self.employee_age < 18:
                self.age_group = 'minor'
            else:
                self.age_group = 'major'

    name = fields.Char(string='Test')
    name_seq = fields.Char(string='Employee Code', required=True, copy=False,
                           readonly=True, index=True, default=lambda self: _('New'))
    gender = fields.Selection([
        ('male', 'Male'),
        ('fe_male', 'Female'),
    ], default='male', string='Gender')
    age_group = fields.Selection([
        ('major', 'Major'),
        ('minor', 'Minor'),
    ], string='Age Group', compute='set_age_group')
    employee_name = fields.Char(string='Name', required=True)
    employee_age = fields.Integer(string='Age')
    notes = fields.Text(string='Registration Notes')
    image = fields.Binary(string='Image', attachment=True)

    @api.model
    def create(self, vals):
        if vals.get('name_seq', _('New')) == _('New'):
            vals['name_seq'] = self.env['ir.sequence'].next_by_code('coffee.employee.sequence') or _('New')
        result = super(CoffeeEmployee, self).create(vals)
        return result
