from odoo import api, fields, models
from odoo.exceptions import ValidationError


class StockMoveInherit(models.Model):
    _inherit = 'stock.move'
    quantity_on_hand = fields.Float(string='Quantity On Hand', related='product_id.qty_available')
    default_code = fields.Char(related='product_id.default_code')
    note_line = fields.Char(string='Note Line')