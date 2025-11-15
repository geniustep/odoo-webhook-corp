{
    'name': 'Auto Webhook Flutter',
    'version': '2.0.0',
    'author': 'Odoo Zak, Odoo SA',
    'depends': [
        'base',
        'sale',
        'product',
        'account',
        'purchase',
        'stock',
        'hr_expense',
        'hr',
    ],
    'description': """Automatic Webhook Registration for Odoo 18 Models with Multi-User Sync Support.
        - Track all model changes automatically
        - Multi-user sync state tracking
        - Smart archiving with automatic cleanup
        - Per-device sync management
        - Supports Sales, Delivery, Manager apps""",
    'summary': 'Auto Webhook with Multi-User Sync & Smart Archiving',
    'category': 'Tools',
    'sequence': 10,
    'website': 'https://www.geniustep.com',
    'license': 'LGPL-3',
    'data': [
        'security/ir.model.access.csv',
        'views/update_webhook_views.xml',
        'views/sync_state_views.xml',
        'views/webhook_menuitem.xml',
        'data/cron_jobs.xml',
    ],
    'installable': True,
    'auto_install': False,
    'application': True,
}
