from odoo import models, fields, api, _


class SchoolClass(models.Model):
    _name = 'school.class'
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _description = 'Class Record'
    _rec_name = 'class_name'

    class_name = fields.Char(string='Name', required=True)
    #kieu list
    is_messy = fields.Boolean(string='Is messy')
    amount_student = fields.Integer(string='Amount Student')
    average_score_class = fields.Compute
    is_great_this_week = fields.Boolean(string='Is Great This Week')

    name_seq = fields.Char(string='Product Code', required=True, copy=False,
                           readonly=True, index=True, default=lambda self: _('New'))


    @api.model
    def create(self, vals):
        if vals.get('name_seq', _('New')) == _('New'):
            vals['name_seq'] = self.env['ir.sequence'].next_by_code('coffee.product.sequence') or _('New')
        result = super(CoffeeProduct, self).create(vals)
        return result
