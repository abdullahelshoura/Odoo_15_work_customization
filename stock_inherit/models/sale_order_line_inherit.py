from odoo import api, fields, models
from odoo.exceptions import ValidationError


class SaleOrderLineInherit(models.Model):
    _inherit = 'sale.order.line'
    stock_id = fields.Many2one('stock.picking')