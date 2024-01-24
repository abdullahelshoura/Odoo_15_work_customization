# -*- coding: utf-8 -*-

from odoo import models, fields, _
from odoo.exceptions import UserError
import base64

class AccountMoveQR(models.Model):
    _inherit = 'account.move'

    # def report_qr_code_receipt(self, order):
    #     def get_qr_encoding(tag, field):
    #         company_name_byte_array = field.encode('UTF-8')
    #         company_name_tag_encoding = tag.to_bytes(length=1, byteorder='big')
    #         company_name_length_encoding = len(company_name_byte_array).to_bytes(length=1, byteorder='big')
    #         return company_name_tag_encoding + company_name_length_encoding + company_name_byte_array
    #
    #     # record = http.request.env['pos.order'].search([('pos_reference', '=', receipt)], limit=1)
    #     qr_code_str = ''
    #     seller_name_enc = get_qr_encoding(1, order.company_id.display_name)
    #     company_vat_enc = get_qr_encoding(2, order.company_id.vat or '')
    #     # date_order = fields.Datetime.from_string(record.create_date)
    #     time_sa = fields.Datetime.context_timestamp(order.with_context(tz='Asia/Riyadh'), order.create_date)
    #     timestamp_enc = get_qr_encoding(3, time_sa.isoformat())
    #     invoice_total_enc = get_qr_encoding(4, str(order.amount_total))
    #     total_vat_enc = get_qr_encoding(5, str(order.currency_id.round(order.amount_tax)))
    #
    #     str_to_encode = seller_name_enc + company_vat_enc + timestamp_enc + invoice_total_enc + total_vat_enc
    #     qr_code_str = base64.b64encode(str_to_encode).decode('UTF-8')
    #     return qr_code_str