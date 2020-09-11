from odoo import models, fields, api, _


class SchoolSemester(models.Model):
    _name = 'school.semester'
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _description = 'Semester Record'
    _rec_name = 'semester_name'

    semester_name = fields.Char(string='Product Code', required=True, copy=False,
                                readonly=True, index=True, default=lambda self: _('New'))
    date_from = fields.Date(string='Date From')
    date_to = fields.Date(string='Date To')
    # time_line_ids
    create_time_line = fields.Date(string='Create Time Line')
