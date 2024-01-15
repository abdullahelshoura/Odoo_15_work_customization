from odoo import api, fields, models,_
from odoo.exceptions import ValidationError


class SaleOrderInherit(models.Model):
    _inherit = 'sale.order'
    maintenance = fields.Boolean(default=False)
    supply_order = fields.Char(string='أمر التوريد')

    @api.model
    def create(self, vals):
        if 'company_id' in vals:
            self = self.with_company(vals['company_id'])
        if vals.get('name', _('New')) == _('New'):
            seq_date = None
            if 'date_order' in vals:
                seq_date = fields.Datetime.context_timestamp(self, fields.Datetime.to_datetime(vals['date_order']))
            if vals['maintenance']:
                vals['name'] = self.env['ir.sequence'].next_by_code('maintenance.order')
                print(vals['name'])
            else:
                vals['name'] = self.env['ir.sequence'].next_by_code('sale.order', sequence_date=seq_date) or _('New')
                print(vals['name'])


        return super(SaleOrderInherit,self).create(vals)

    def action_confirm(self):
        if self.maintenance == True:
            for line in self.order_line:
                prod_temp = self.env['product.template'].search([('name', '=', line.product_id.name)])
                if prod_temp.invoice_policy == 'order':
                    continue
                else:
                    prod_temp.invoice_policy = 'order'
                    prod_temp.check_invoice_policy_change=True
        super(SaleOrderInherit, self).action_confirm()
