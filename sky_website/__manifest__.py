# -*- encoding: utf-8 -*-
#########################################################################################
#
#    Copyright (C) 2019 Skyscend Business Solutions (https://www.skyscendbs.com)
#    Copyright (C) 2020 Skyscend Business Solutions  Pvt. Ltd.(<https://skyscendbs.com>)
#
#########################################################################################

{
    'name': 'Sky Website',
    'version': '16.0.0.1',
    'license': 'AGPL-3',
    'description': """
        Sky Website
    """,
    'author': 'Skyscend Business Solutions Pvt. Ltd.',
    'website': 'https://www.skyscendbs.com',
    'depends': [
        'website'
    ],
    'data': [
        'views/home_sky_website_template.xml',
        'views/services_template.xml',
        'views/training_template.xml',
        'views/about_us_template.xml',
        'views/contact_us_template.xml',

    ],
    'assets': {
        'web.assets_frontend': [
            'sky_website/static/src/scss/sky_website.scss',
        ],
    },
    'installable': True,
}
