# -*- coding: utf-8 -*-
##############################################################################
#
#    ODOO Open Source Management Solution
#
#    ODOO Addon module by Uncanny Consulting Services LLP
#    Copyright (C) 2023 Uncanny Consulting Services LLP (<https:/uncannycs.com>).
#
##############################################################################
{
    'name': "Purchase Reminder",
    'summary': "Purchase Quotation Due Date Reminder",
    'description': """Purchase Quotation Due Date Reminder Odoo application helps businesses manage purchase quotations efficiently by adding a due date and sending automated email reminders""",
    "version": "18.0",
    "category": "Extra Tools",
    "website": "https://uncannycs.com",
    "author": "Uncanny Consulting Services LLP",
    "maintainers": "Uncanny Consulting Services LLP",
    "license": "Other proprietary",
    'website': "https://www.yourcompany.com",
    'depends': ['base','purchase','mail'],
    'data': [
        'security/ir.model.access.csv',
        'data/check_due_date_cron.xml',
        'views/due_date_email_template.xml',
        'views/puchase_order_view.xml',
    ],
    "images": ['static/description/banner.gif'],
    "application": False,
    "installable": True,
    "auto_install": False,
}
