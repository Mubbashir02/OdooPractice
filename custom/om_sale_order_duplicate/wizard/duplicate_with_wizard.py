from odoo import fields, models, api


class duplicate_with_wizard(models.TransientModel):
    _name = 'sale.order.wizard'
    _description = 'Duplicate Sale Order Wizard'


    def dupliate_action_button(self):
        self.env['sale.order'].browse(self.env.context.get('active_id')).duplicate_state()








