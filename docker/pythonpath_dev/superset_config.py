from flask_appbuilder.security.manager import AUTH_OAUTH

SECRET_KEY='xQXsITfo74ALPPAcC6i5yRiQZOFjULAv0QgPEUA57k0jl0RZ70HKSPJP'

# Enable OAuth authentication
AUTH_TYPE = AUTH_OAUTH
LOGOUT_REDIRECT_URL='http://192.168.75.80:8081/realms/superset/protocol/openid-connect/logout'
AUTH_USER_REGISTRATION = True
AUTH_USER_REGISTRATION_ROLE = 'Gamma'
# OAuth provider configuration for Keycloak
OAUTH_PROVIDERS = [
    {
        'name': 'keycloak',
        'icon': 'fa-key',
        'token_key': 'access_token',  # Keycloak uses 'access_token' for the access token
        'remote_app': {
            'client_id': 'superset',
            'client_secret': '7C53Swu1oDoloQQgFlcUJuWbQBX6gRTH',
            'client_kwargs': {
                'scope': 'openid profile email',
            },
            'server_metadata_url': 'http://192.168.75.80:8081/realms/superset/.well-known/openid-configuration',
            'api_base_url': 'http://192.168.75.80:8081/realms/superset/protocol/',
        },
    }
    ]
