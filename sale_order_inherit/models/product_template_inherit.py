from odoo import api, fields, models,_
from odoo.exceptions import ValidationError

class ProductTemplateInherit(models.Model):
    _inherit = 'product.template'

    check_invoice_policy_change = fields.Boolean(default=False)
