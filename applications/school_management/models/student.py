from audioop import avg

from odoo import models, fields, api, _


class SchoolStudent(models.Model):
    _name = 'school.student'
    _description = 'Student Record'
    _rec_name = 'student_name'

    @api.depends('math_object', 'physic_subject', 'chemistry_subject')
    def _compute_average_subjects(self):
        for record in self:
            record.average_subjects = avg(record.math_subject + record.physic_subject + record.chemistry_subject)

    student_name = fields.Char(string='Name', required=True)
    class_id = fields.Many2one(string='Id of Class')
    student_age = fields.Integer(string='Age')
    math_subject = fields.Float(string='Score of Math')
    physic_subject = fields.Float(string='Score of Physic')
    chemistry_subject = fields.Float(string='Score of Chemistry')
    average_subjects = fields.Float(compute='_compute_average_subjects')


