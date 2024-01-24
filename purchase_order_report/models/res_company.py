# -*- coding: utf-8 -*-
from odoo import models, fields, _

class Partner(models.Model):
    _inherit = 'res.company'

    name = fields.Char(related='partner_id.name', string='Company Name', required=True, store=True, readonly=False, translate=True)
    street = fields.Char(translate=True)
    street2 = fields.Char(compute='_compute_address', inverse='_inverse_street2', translate=True)
    zip = fields.Char(compute='_compute_address', inverse='_inverse_zip', translate=True)
    city = fields.Char(compute='_compute_address', inverse='_inverse_city', translate=True)
    vat = fields.Char(related='partner_id.vat', string="Tax ID", readonly=False,translate=True)
    company_registry = fields.Char(compute='_compute_company_registry', store=True, readonly=False,translate=True)
