from odoo import models, fields


class HospitalPatient(models.Model):
    _name = 'hospital.patient'  # This is the technical ID
    _description = 'Hospital Patient'

    name = fields.Char(string="Patient Name", required=True)
    age = fields.Integer(string="Age")
    gender = fields.Selection([('male', 'Male'), ('female', 'Female')], string="Gender")
    medical_history = fields.Text(string="Medical History")


 