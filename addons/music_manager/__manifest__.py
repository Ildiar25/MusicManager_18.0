# -*- coding: utf-8 -*-
# Copyright (C) 2026 Joan Pastor
# License LGPL-3.0 or later (https://www.gnu.org/licenses/lgpl-3.0.html).

# noinspection PyStatementEffect
{
    'name': "Music Manager",
    'version': "2.0.0",
    'category': "Music Manager",
    'description': """
        This module allows the user to manage a music directory, doing CRUD operations with music files and
        update music metadata with ID3 labels.
    """,
    'author': "Joan Pastor",
    'website': "",
    'depends': [
        "base",
        "web"
    ],
    'assets': {
        # 'web.assets_backend': [
        #     'music_manager/static/src/css/styles.css'
        # ]
    },
    'data': [
        # Security
        # "security/music_manager_groups.xml",
        # "security/ir.model.access.csv",

        # Views
        "views/res_config_settings_views.xml",

        # Wizards
        # "views/music_manager_change_owner_wizard_views.xml",
        # "views/music_manager_track_wizard_views.xml",

        # Menus
        # "views/music_manager_menus.xml",

        # Triggered actions
        # "data/ir_cron_data.xml",
    ],
    'installable': True,
    'application': True,
    'auto_install': False,
    'license': "LGPL-3",
}