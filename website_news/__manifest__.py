# -*- coding: utf-8 -*-
{
    'name': "Website News",

    'author': "Deja-Vu",
    'website': "http://www.deja-vu.com/",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/13.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Website',
    'version': '13',

    # any module necessary for this one to work correctly
    'depends': ['base', 'web', 'mail', 'website_blog', 'website'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        # 'views/news.xml',
        'views/website_blog.xml',
        'views/blog_blog.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}
