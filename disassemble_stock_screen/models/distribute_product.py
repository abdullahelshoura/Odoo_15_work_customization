from odoo import models, fields, api, _
from odoo.exceptions import UserError

class DistributeProduct(models.Model):
    _name = 'distribute.product'

    name = fields.Char('Reference', copy=False, readonly=True, default=lambda x: _('New'))
    stock_delivery_id = fields.Many2one('stock.picking.type', string='Delivery OP')
    stock_receipt_id = fields.Many2one('stock.picking.type', string='Receipt OP')
    sale_order_id = fields.Many2one('sale.order', string='Sale Order')
    partner_id = fields.Many2one('res.partner', string='Customer')
    work_order = fields.Char(string='Work Order')
    product_id = fields.Many2one('product.product', string='Product', required=True)
    quantity = fields.Integer(string='Qty', required=True, default='1')
    distribute_product_line_ids = fields.One2many('distribute.product.line', 'distribute_product_id')
    state = fields.Selection([('draft', 'Draft'), ('confirmed', 'Confirmed')], string='State',
                             default='draft', index=True)

    @api.model
    def create(self, vals):
        vals['name'] = self.env["ir.sequence"].next_by_code("distribute.product")
        return super(DistributeProduct, self).create(vals)

    @api.onchange('sale_order_id')
    def _get_customer(self):
        if self.sale_order_id:
            self.partner_id = self.sale_order_id.partner_id
        else:
            self.partner_id = False

    def action_confirm(self):
        for rec in self:
            virtual_location = self.env['stock.location'].search([('usage', '=', 'production')], limit=1)
            move = self.env['stock.move'].create({
                'name': 'Disaasemble Move',
                'location_id': rec.stock_delivery_id.default_location_src_id.id,
                'location_dest_id': virtual_location.id,
                'product_id': rec.product_id.id,
                'product_uom': rec.product_id.uom_id.id,
                'product_uom_qty': rec.quantity,
                'quantity_done': rec.quantity,
            })
            move._action_confirm()
            move._action_done()
            for line in rec.distribute_product_line_ids:
                line_move = self.env['stock.move'].create({
                    'name': 'Disaasemble Move Line',
                    'location_id': virtual_location.id,
                    'location_dest_id': line.distribute_product_id.stock_receipt_id.default_location_dest_id.id,
                    'product_id': line.product_id.id,
                    'product_uom': line.product_id.uom_id.id,
                    'product_uom_qty': line.quantity,
                    'quantity_done': line.quantity,
                })
                line_move._action_confirm()
                line_move._action_done()
            rec.state = 'confirmed'






class DistributeProductLine(models.Model):
    _name = 'distribute.product.line'

    distribute_product_id = fields.Many2one('distribute.product')
    product_id = fields.Many2one('product.product', string='Product', required=True)
    quantity = fields.Integer(string='Qty', default='1')


