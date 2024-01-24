# -*- coding: utf-8 -*-
from odoo import models, fields,api, _

class PurchaseOrder(models.Model):
    _inherit = 'purchase.order'

    week_number = fields.Integer(string='Week Number', compute='_compute_week_number')
    remarks = fields.Char(string='Remarks')

    @api.onchange('date')
    def _compute_week_number(self):
        for record in self:
            if record.date_approve:
                # Calculate the ISO week number
                iso_week_number = record.date_approve.isocalendar()[1]
                record.week_number = iso_week_number
            else:
                record.week_number = 0