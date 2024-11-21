# -*- coding: utf-8 -*-
{

    'name': "Quickbooks Odoo Connector",

    'summary': """
        Quickbooks Odoo Connector supports two-way synchronization which makes management a lot more easier! 
        Our module helps you integrate and manage your Quickbooks Online with Odoo. 
        Sync Quickbooks and Odoo with just one click.""",

    'description': """
        - Ixport and Emport data to and from Quickbooks Online.
        - For enabling Chart Of Accounts, activate accounting features by enabling the option in user settings.
    """,

    'author': "Techspawn Solutions Pvt Ltd",
    'website': "http://www.techspawn.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/master/openerp/addons/base/module/module_data.xml
    # for the full list
    'license':'OPL-1',
    'category': 'custom',
    'version': '17.0.1.0.0',

    # any module necessary for this one to work correctly
    'depends': ['base', 'sale', 'sale_management', 'stock', 'purchase', 'hr'],

    'assets': {
        'web.assets_frontend': [
            "quickbooks_odoo_connector/static/description/assets/src/js/index_file.js",
            
        ]},

    'price': 200.00,
    # 'price': 160.00,
    'currency': 'USD',

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'security/security_view.xml',
        'views/message_wizard.xml',
        'views/backend.xml',
        'views/customer_vendor.xml',
        'views/product_quick.xml',
        'views/payment_term_view.xml',
        'views/quick_account.xml',
        'views/employee_form.xml',
        'views/sync_all.xml',
        'views/schedule_refresh_token.xml',
        'views/jobs_view.xml'
    ],
    'external_dependencies': {
        'python': ['requests_oauthlib'],
    },
    
    "images": ['static/description/Odoo-v17.gif'],
    # "images": ['static/description/15aug_2024_sale.jpg'],
    'installable': True,
    'application': True,

    
}
