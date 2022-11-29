from odoo import models, fields, api
from odoo.exceptions import ValidationError



class HospitalManagmentSystem(models.Model):
    _name = 'hopistalsystem.patient'
    _description = 'Patient Record Syste,'
    # _inherit = ['mail.thread','mail.activity.mixin']
    # _rec_name = 'patient_name'

    # @api.constrains('patient_age')
    # def check_age(self):
    #     for rec in self:
    #         if rec.patient_age <=5:
    #             raise ValidationError("Age is Greater than 5")
    #
    # @api.depends('patient_age')
    # def set_age_group(self):
    #     for rec in self:
    #         if rec.patient_age:
    #             if rec.patient_age < 18:
    #                 rec.age_group = 'minor'
    #             else:
    #                 rec.age_group = 'major'
    #         else:
    #             rec.age_group = ''


    patient_name = fields.Char(string='Name', required = True)
    patient_age = fields.Integer(string='Age')
    notes = fields.Text(string='Notes')
    image = fields.Binary(string='Image')
    age_group = fields.Selection([('major','MAJOR'),
                                  ('minor','MINOR'),
                                  ],string="Age Group", compute="set_age_group")

# class saletoinherit(models.Model):
#     _inherit = 'sale.order'
#     patient_group = fields.Char(string="Patient Name")
#
#
#
#
#
# class hopistaltocontact(models.Model):
#     _inherit = 'res.partner'
#     patient_group = fields.Char()