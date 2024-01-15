# -*- coding: utf-8 -*-
{
    'name': "disassemble_stock_screen",
    'summary': """ Disassemble Stock Screen Model """,
    'author': 'IBS Company',
    'category': 'Inventory',
    'version': '0.1',
    'depends': ['base', 'mrp', 'stock', 'sale', 'product'],
    'data': [
        'security/ir.model.access.csv',
        'data/sequence_data.xml',
        'views/distribute_product_view.xml',
    ],
    'license': 'LGPL-3',
}


