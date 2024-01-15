import re
from re import match

from odoo import api, fields, models
from odoo.exceptions import ValidationError


class StockPickingInherit(models.Model):
    _inherit = 'stock.picking'
    # customer = fields.Many2one('sale.order')


    work_order = fields.Char(string='Work Order')

    picking_type_receipt = fields.Boolean(related='picking_type_id.receipt_type_rec')
    picking_type_delivery = fields.Boolean(related='picking_type_id.receipt_type_del')
    picking_type_internal = fields.Boolean(related='picking_type_id.receipt_type_int')
    olines = fields.One2many('order.lines.trans','stock_id')


    so = fields.Many2one('sale.order', string='Sale Order')

    internal_type = fields.Many2many('stock.picking','relational_table_name','stck_pick_1' ,string='Internal Type')
    internal_length = fields.Boolean(compute='compute_internal_length')
    so_lines = fields.One2many('sale.order.line', 'stock_id')



    @api.depends('internal_type')
    def compute_internal_length(self):
        for rec in self:
            length = False
            if rec.internal_type:
                length = True
            rec.internal_length = length


    @api.onchange('internal_length')
    def clear_operations(self):
        if not self.internal_length:
            self.move_ids_without_package = [(5,0,0)]
            self.move_line_ids_without_package = [(5,0,0)]
            print("Noooo")


    @api.onchange('partner_id')
    def onchange_partner_id(self):
        for rec in self:
            return {'domain': {'so': [('partner_id', '=', rec.partner_id.id)]}}


    @api.onchange('so')
    def insert_so_lines(self):
        # check if we are already standing in the multiple create invoices view
        if self.so:
                lines = self.env['sale.order.line'].search([('order_id', '=', self.so.id)])

                # delete all records from view
                orders_lines = [(5, 0, 0)]

                for order_line in lines:
                    # print(order.name)
                    # delete_all_records = (5, 0, 0)
                    line = (0, 0, {
                        'product_id': order_line.product_id,
                        'product_qty': order_line.product_uom_qty
                    })
                    # # orders_lines.append(delete_all_records)
                    # record_set = self.env['order.invoice.data'].search([])
                    # record_set.unlink()

                    orders_lines.append(line)

                    # print(self.env['order.invoice.data'].search([]))
                self.olines= orders_lines
        return {'domain': {'internal_type': [('so', '=', self.so.id), ('state', '=', 'done')]}}


    @api.onchange('internal_type')
    def insert_operation_lines(self):
        if self.internal_type:
            for rec in self:
                rec.move_ids_without_package = False
                rec.move_line_ids_without_package = False
                for res in rec.internal_type:
                    for ex in res.move_ids_without_package:
                        rec.move_ids_without_package = [(0, 0, {
                            'name': ex.name,
                            'product_id': ex.product_id.id,
                            'product_uom': ex.product_uom,
                            'location_id': ex.location_id,
                            'location_dest_id': ex.location_dest_id,
                            'note_line': ex.note_line,
                            'state': 'draft',
                        })]
                        rec.move_line_ids_without_package = [(0, 0, {
                            # 'name': ex.name,
                            'product_id': ex.product_id.id,
                            'location_id': ex.location_id,
                            'location_dest_id': ex.location_dest_id,
                            'state': 'draft',
                        })]

class StockPickingInherit(models.Model):
    _inherit = 'stock.picking.type'

    receipt_type_rec = fields.Boolean(string='إذن صرف و إضافة', default=False)
    receipt_type_del = fields.Boolean(string='إذن تسليم مخزن صيانة', default=False)
    receipt_type_int = fields.Boolean(string='التحويلات الداخلية', default=False)


class OrderLinesTrans(models.Model):
    _name = 'order.lines.trans'

    stock_id = fields.Many2one('stock.picking')
    product_id = fields.Many2one('product.product', string='Product')
    product_qty = fields.Float(string='Quantity')

