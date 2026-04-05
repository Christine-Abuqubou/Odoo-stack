from odoo import models, fields, api    

class SchoolClass(models.Model):
    _name='school.class'
    _description='School Class'
    
    name=fields.Char(string="Class Name")
    
    student_ids=fields.One2many('student.student', 'class_id', string="Students")
    
    