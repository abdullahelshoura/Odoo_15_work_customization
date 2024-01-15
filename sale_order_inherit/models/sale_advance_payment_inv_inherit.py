from odoo import api, fields, models
from odoo.exceptions import ValidationError


class SaleAdvancePaymentInvInherit1(models.TransientModel):
    _inherit = "sale.advance.payment.inv"

    def create_invoices(self):
        sale_orders = self.env['sale.order'].browse(self._context.get('active_ids', []))
        for rec in sale_orders:
            for line in rec.order_line:
                prod_temp = self.env['product.template'].search([('name', '=', line.product_id.name)])
                if prod_temp.check_invoice_policy_change:
                    prod_temp.invoice_policy = 'delivery'
                    prod_temp.check_invoice_policy_change = False
        return super(SaleAdvancePaymentInvInherit1, self).create_invoices()
