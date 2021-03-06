# -*- coding: utf-8 -*-
{
    'name': "Auth OAuth Keycloak",

    'summary': """
        Enables Keycloack integration for the OAuth2 Authentication module.
    """,

    'description': """
        Enables Keycloack integration for the OAuth2 Authentication module.
    """,

    'author': 'Mint System',
    'website': 'https://www.mint-system.ch',
    'license': 'AGPL-3',
    'category': 'Technical Settings',
    'version': '13.0.1.0.5',

    'depends': [
        'base',
        'auth_oauth',
    ],

    'data': [
        'views/ir_model_fields.xml',
        'views/ir_ui_view.xml',
        'data/auth_oauth_keycloak_data.xml'
    ],
}
