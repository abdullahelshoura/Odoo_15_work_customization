# Copyright 2018 Tecnativa - Carlos Dauden
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).
{
    'name': 'Stock Picking Edit',
    'summary': 'stock_picking_edit',
    'version': '0.1',
    'category': 'stock_picking_edit',
    'website': 'https://github.com/OCA',
    'author': 'Tecnativa, Odoo Community Association (OCA)',
    'license': 'AGPL-3',
    'depends': [
        'base', 'stock','sale',
    ],
    'data': [
        'security/ir.model.access.csv',
        'views/stock_views_inherit.xml',
        'reports/sale_order_report.xml'

    ],
}
