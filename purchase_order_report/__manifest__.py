# Copyright 2018 Tecnativa - Carlos Dauden
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).
{
    'name': 'Purchase Report Edit',
    'summary': 'purchase_report_edit',
    'version': '0.1',
    'category': 'purchase_report_edit',
    'website': 'https://github.com/OCA',
    'author': 'Tecnativa, Odoo Community Association (OCA)',
    'license': 'AGPL-3',
    'depends': [
        'base', 'purchase',
    ],
    'data': [
        'views/purchase_order_inherit.xml',
        'views/po_inherit_view.xml',

    ],

}
