# -*- coding: utf-8 -*-
##############################################################################
#
#    OpenERP, Open Source Management Solution
#    Copyright (C) 2018 Mostafa Abd El Fattah ERP Consultant (<mostafa.ic2@gmail.com>).
#
#    For Module Support : mostafa.ic2@gmail.com  or Skype : mostafa.abd.elfattah1
#    This Module Extended from IT Libertas
##############################################################################
{
    'name': 'Fire Notifications',
    'version': '12.0.1.0',
    'sequence':1,
    'category': 'Generic Modules/Inventory',
    'summary': 'Using Notification fire for other modules',
    'description': """ 
        The app is a tool of generating popups similar to calendar events alarms in your own modules
        Extended the idea from IT Libertas
    """,
    'author': 'Mostafa Abd El Fattah<mostafa.ic2@gmail.com>', 
    'website': 'https://www.linkedin.com/in/mabdelfattah1/',
    'images': ['images/main.png'],
    'depends': ['base'],
    'data': [
       'security/ir.model.access.csv',
        'views/popup_notifications.xml',
    ],
    'qweb': [
        'static/xml/base_popup.xml',
            ],
    'test': [],
    'installable':True,
    'application':True,
    'auto-install':False,
    'price':9.99,
    'currency':'EUR', 
}
