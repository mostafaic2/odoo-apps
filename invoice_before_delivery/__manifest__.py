# -*- coding: utf-8 -*-
##############################################################################
#
#    OpenERP, Open Source Management Solution
#    Copyright (C) 2018 Mostafa Abd El Fattah ERP Consultant (<mostafa.ic2@gmail.com>).
#
#    For Module Support : mostafa.ic2@gmail.com  or Skype : mostafa.abd.elfattah1
#
##############################################################################
{
    'name': 'Invoice Before Delivery',
    'version': '12.0.1.0',
    'sequence':1,
    'category': 'Generic Modules/Sales Management',
    'summary': 'this module will prevent the delivery order from being created until the invoice is validated',
    'description': """ 

       
    """,
    'author': 'Mostafa Abd El Fattah<mostafa.ic2@gmail.com>', 
    'website': 'http://www.demo.com',
    'images': ['images/main_screenshot.jpg'],
    'depends': ['sale', 'purchase', 'stock', 'account'],
    'data': [
        'views/sale_view.xml',
    ],
    'test': [],
    'installable':True,
    'application':True,
    'auto-install':False,
    'price':25.0,
    'currency':'EUR', 
}
