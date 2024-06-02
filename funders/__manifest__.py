{
    'name': 'funders',
    'version': '17.0',
    'category': 'funders',
    'depends': ['crm'],
    "author": 'INKERP',
    'website': "https://www.INKERP.com",

    'data': [
        'security/ir.model.access.csv',
        'data/data.xml',
        'wizard/update_crm_tag_view.xml',
        'views/crm_menu_inherit.xml',
        'views/tree_button.xml',
    ],
    'assets': {
            'web.assets_backend': [
                # 'funders/static/src/js/tree_button.js',
            ],
        },

    'images': ['static/description/banner.png'],
    'license': "OPL-1",
    'installable': True,
    'application': True,
    'auto_install': False,
}
