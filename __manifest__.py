# -*- coding: utf-8 -*-
{
    'name'     : 'InfoSaône - Module Odoo 14 pour JuratelPro',
    'version'  : '14.0.0.1',
    'author'   : 'InfoSaône',
    'category' : 'InfoSaône',
    'description': """
InfoSaône - Module Odoo 14 pour JuratelPro
===================================================
""",
    'maintainer' : 'InfoSaône',
    'website'    : 'http://www.infosaone.com',
    'depends'    : [
        'base',
        'account',
        'calendar',
    ],
    'data' : [
        'security/ir.model.access.csv',
        'views/calendar_views.xml',
    ],
    'installable': True,
    'application': True,
}
