from odoo import api, fields, models
from odoo.exceptions import ValidationError


class SaleOrderLineInherit(models.Model):
    _inherit = 'sale.order.line'

    default_code = fields.Char(string='Internal Reference', related='product_id.default_code')
    note_line = fields.Char(string='Note Line')
    quantity_on_hand = fields.Float(string='Quantity On Hand', related='product_id.qty_available')
