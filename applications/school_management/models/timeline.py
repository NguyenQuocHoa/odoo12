from odoo import models, fields, api, _


class SchoolWeek(models.Model):
    _name = 'school.time_line'
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _description = 'Time Line Record'
    _rec_name = 'this_week'

    @api.depends('semester_id')
    def _select_date_from(self):
        pass

    @api.depends('SchoolSemester.date_from', 'date_to')
    def _compute_this_week(self):
        for record in self:
            record.this_week = (record.date_to - SchoolSemester.date_to) / 7

    date_from = fields.Date(string='Date From')
    date_to = fields.Date(string='Date To')
    #time_line_ids
    semester_id = fields.Many2one(string='Semester Id')
    this_week = fields.Integer(compute='_compute_this_week')
