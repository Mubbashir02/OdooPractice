from odoo import models, fields, api



class Hospitalappoinment(models.Model):
    _name = 'hopistal.appoinment'
    _description = 'appoinment '


    patient_id = fields.Many2one('hopistal.patient',string='Paitent ', required=True)
    patient_age = fields.Integer(string='Age', related='patient_id.patient_age')
    notes = fields.Text(string='Notes')
    appoinmentdates = fields.Date(string='Dates', required=True)

