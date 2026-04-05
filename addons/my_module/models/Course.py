from odoo import models, fields, api

class Course(models.Model):
    _name = 'school.course'
    _description = 'School Course'
    
    name = fields.Char(string="Course Name")
    description = fields.Text(string="Course Description")
    
    student_ids = fields.Many2many('student.student', string="Students")