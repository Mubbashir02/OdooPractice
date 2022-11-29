from odoo import fields, models, api


class sale_order_duplication(models.Model):
    _inherit = 'sale.order'

    def duplicate_state(self):
        print('helllo')
        # self.env['product.product'].search(['|',(['&&',('id','>',50),('unit_price','>=',0)]),('cost','>',100)])
        # print(self.env['product.product'].search_count([]))
        # print(self.env['product.product'].search_count([('lst_price','>',23500)]))
        # #normal
        # rec = self.env['sale.order'].create({
        #     'partner_id': self.partner_id.id,
        #     'validity_date': self.validity_date,
        #     'date_order': self.date_order,
        #     'payment_term_id': self.payment_term_id.id,
        #     'sale_order_template_id': self.sale_order_template_id.id,
        #
        #     # for on to many purpose
        #      'order_line' : [(0,0, {
        #         'product_id': self.order_line[i].product_id.id,
        #         'product_uom_qty': self.order_line[i].product_uom_qty,
        #          'price_unit': self.order_line[i].price_unit,
        #      }) for i in range(len(self.order_line))]
        #
        #
        # })
        # #for many to many purpose
        # for x,y in zip(self.order_line,rec.order_line):
        #     y.tax_id = x.tax_id
        # # rec.order_line = self.order_line
        # for x in range(1):
        #     self.duplicate_reference = rec.id
        # return{
        #     'res_model': 'sale.order',
        #     'res_id': self.duplicate_reference.id ,
        #     'type': 'ir.actions.act_window',
        #     'view_mode': 'form',
        #     'view_id': self.env.ref('sale.view_order_form').id,
        #
        # }

    duplicate_reference = fields.Many2one('sale.order', readonly=True)
    product_count = fields.Integer()




