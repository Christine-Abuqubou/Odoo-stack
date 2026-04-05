from odoo import models, fields
 
class Student(models.Model):
    _name = 'student.student'
    _description = 'Student'
 
    name = fields.Char(string="Name")
    age = fields.Integer(string="Age")
    email = fields.Char(string="Email")
    
    class_id = fields.Many2one('school.class', string="Class")
    course_ids=fields.Many2many('school.course', string="Courses")
    
    
    