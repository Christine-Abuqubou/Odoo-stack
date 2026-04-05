# -*- coding: utf-8 -*-

# from odoo import models, fields, api


# class my_module(models.Model):
#     _name = 'my_module.my_module'
#     _description = 'my_module.my_module'

#     name = fields.Char()
#     value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         for record in self:
#             record.value2 = float(record.value) / 100

from odoo import models, fields, api


class SaleOrder(models.Model):
    _inherit = 'sale.order'

    test_custom_note = fields.Selection([
        ('urgent', 'Urgent Delivery'),
        ('fragile', 'Fragile Handle with Care'),
        ('gift', 'Gift Wrap Required')
    ], string="Shipping Note", default='urgent')

    @api.onchange('partner_id')
    def _onchange_partner_id_shipping_note(self):
        if self.partner_id and self.partner_id.is_company:
            self.test_custom_note = 'urgent'
        else:
            self.test_custom_note = 'gift'


    # New Field
    note_count = fields.Integer(string="Note Length", compute="_compute_note_count")

    @api.depends('test_custom_note')
    def _compute_note_count(self):
        for record in self:
            if record.test_custom_note:
                record.note_count = len(record.test_custom_note)
            else:
                record.note_count = 0
                
                
                
                




# class SaleOrder(models.Model):
#     _inherit= 'sale.order'
    
    # test_custom_note=fields.Char(string="Custom  Mac Note")