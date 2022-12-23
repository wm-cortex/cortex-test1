# -*- coding: utf-8 -*-
# Copyright 2020 CorTex IT Solutions Ltd. (<https://cortexsolutions.net/>)
# License OPL-1
{
    'name': "Ecommerce - Payment Methods per Product",
    'summary': """
        Show payment methods in ecommerce per Acquirers assigned to the purchase products.
        """,
    'description': """
    Website Payment Acquirer Filter per Product
    Payment Acquirer
    Filter Payment Acquirer
    Filter Payment Acquirer per product
    Payment Methods per Product
    Ecommerce Payment Methods per Product
    """,

    'author': 'CorTex IT Solutions Ltd.',
    'website': 'https://cortexsolutions.net',
    'license': 'OPL-1',
    'support': 'support@cortexsolutions.net',
    'currency': 'EUR',
    'price': 70,
    # Categories can be used to filter modules in modules listing
    # for the full list
    'category': 'eCommerce',
    'version': '1.0.0',

    # any module necessary for this one to work correctly
    'depends': ['website_sale',
                'website_payment'],
    # always loaded
    'data': [
        'views/product_template_views.xml',
    ],
    'images': ['static/description/main_screenshot.png'],
    "installable": True,
    'auto_install': False,
    'application': False,
}
