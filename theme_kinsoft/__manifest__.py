{
    'name': 'Kinsoft Theme',
    'description': 'Kinsoft Theme - Business, Odoo Implementator, Odoo ERP',
    'category': 'Theme/Services',
    'sequence': 220,
    'version': '1.0',
    'depends': [
        'website',
        'website_theme_install',
        'theme_bootswatch',
        'website_blog',
        'website_animate',
        'website_odoo_debranding',
        'gtica_whatsapp_live_free'],
    'data': [
        #'views/layout.xml',
        #'views/pages.xml',
        # 'views/website_menu.xml',
        'views/assets.xml'
    ],
    'images': [
        'static/description/kinsoft.png',
        'static/description/kinsoft_screenshot.jpg',
    ],
    'license': 'LGPL-3',
    'live_test_url': 'https://kinsoft.id'
}
