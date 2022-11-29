from odoo import models, fields, api
from odoo.exceptions import ValidationError



class HospitalManagment(models.Model):
    _name = 'hopistal.patient'
    _description = 'Patient Record'
    # _inherit = ['mail.thread','mail.activity.mixin']
    _rec_name = 'patient_name'

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
    def open_patient_opppoinment(self):
        return{
            'name': 'Appoinment',
            'domain': [('patient_id', '=', self.id)],
            'view_type': 'form',
            'res_model': 'hopistal.appoinment',
            'view_id': False,
            'view_mode': 'tree,form',
            'type': 'ir.actions.act_window',
        }
    def counter_function(self):
        count = self.env['hopistal.appoinment'].search_count([('patient_id', '=', self.id)])
        self.oppoinment_count = count
    patient_name = fields.Char(string='Name', required = True)
    patient_age = fields.Integer(string='Age', track_visibility="always")
    notes = fields.Text(string='Notes')
    image = fields.Binary(string='Image')
    oppoinment_count = fields.Integer(string='Count',compute='counter_function')
    # age_group = fields.Selection([('major','MAJOR'),
    #                               ('minor','MINOR'),
    #                               ],string="Age Group")

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
