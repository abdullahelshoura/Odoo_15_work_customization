# -*- coding: utf-8 -*-
from odoo import models, fields, _

class Partner(models.Model):
    _inherit = 'res.partner'

    name = fields.Char(index=True, translate=True)
    street = fields.Char(translate=True)
    street2 = fields.Char(translate=True)
    zip = fields.Char(change_default=True,translate=True)
    city = fields.Char(translate=True)
    nickname= fields.Char(translate=True)
