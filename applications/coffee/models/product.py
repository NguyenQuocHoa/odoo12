from odoo import models, fields, api, _


class CoffeeProduct(models.Model):
    _name = 'coffee.product'
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _description = 'Product Record'
    _rec_name = 'product_name'

    product_name = fields.Char(string='Name', required=True)
    price = fields.Integer(string='Price')
    status = fields.Char(string='Status')
    notes = fields.Text(string='Notes')
    image = fields.Binary(string='Image')
    name_seq = fields.Char(string='Product Code', required=True, copy=False,
                           readonly=True, index=True, default=lambda self: _('New'))
    is_expired = fields.Boolean()

    @api.model
    def create(self, vals):
        if vals.get('name_seq', _('New')) == _('New'):
            vals['name_seq'] = self.env['ir.sequence'].next_by_code('coffee.product.sequence') or _('New')
        result = super(CoffeeProduct, self).create(vals)
        return result
