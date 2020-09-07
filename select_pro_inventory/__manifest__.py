# -*- coding: utf-8 -*-
{
    'name': "Select Multi Product Inventory",
    'version': '13',
    'category': 'Inventory',
    'license': '',
    'author': "Deja-Vu",
    'website': "http://www.deja-vu.com/",

    # any module necessary for this one to work correctly
    'depends': ['base', 'stock'],

    # always loaded
    'data': [
        'wizard/stock_move_wizard_view.xml',
        'wizard/stock_move_line_wizard_view.xml',
        'views/select_products.xml',
    ],
}
