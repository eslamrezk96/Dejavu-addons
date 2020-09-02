# -*- coding: utf-8 -*-
{
    'name': "select_multi_pro_inventory",

    # any module necessary for this one to work correctly
    'depends': ['base', 'stock'],

    # always loaded
    'data': [
        'wizard/select_products_wizard_view.xml',
        'views/select_products.xml',
    ],
}
