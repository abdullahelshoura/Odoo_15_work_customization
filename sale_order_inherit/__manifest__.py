# Copyright 2018 Tecnativa - Carlos Dauden
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).
{
    'name': 'Sale Order Inherit',
    'summary': 'sale_order_inherit',
    'version': '0.1',
    'category': 'sale_order_inherit',
    'website': 'https://github.com/OCA',
    'author': 'Tecnativa, Odoo Community Association (OCA)',
    'license': 'AGPL-3',
    'depends': [
        'base','sale_management','sale','sale_stock' ,
    ],
    'data': [
        'data/sequence_data.xml',
        'views/sale_order_views_inherit.xml',


    ],
}
