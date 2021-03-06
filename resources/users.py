from flask import current_app as app
from eve.auth import BasicAuth
from hashlib import sha1
from datetime import datetime


class AuthByLoginAndPass(BasicAuth):
    def check_auth(self, username, password, allowed_roles, resource, method):
        users = app.data.driver.db['users']
        user = users.find_one({'username': username})
        return user and password == user['pass']


def add_user_defaults(documents):
    for document in documents:
        document['token'] = sha1((document['username'] + document['pass'] +
                                 str(datetime.now())).encode('utf-8')).hexdigest()
        document['role'] = 'user'
        document['status'] = 0
        document['deleted'] = 0

# Описываем ресурс `/users`
USERS = {
    # the standard account entry point is defined as
    # '/accounts/<ObjectId>/'. We define  an additional read-only entry
    # point accessible at '/accounts/<username>/'.
    'additional_lookup': {
        'url': 'regex("[\w]+")',
        'field': 'username',
    },

    'public_methods': ['POST'],
    'public_item_methods': [],

    'allowed_roles': ['user', 'admin'],

    # Здесь мы описываем модель данных. Для валидации используется модуль Cerberus от автора Eve.
    # Вы можете ознакомиться с ним в официальной документации модуля http://docs.python-cerberus.org/en/stable/.
    # Либо прочитать заметки в официальной документации EVE http://python-eve.org/validation.html#validation.
    'schema': {
        # _id added automatically by eve
        # _created (reg date) added automatically by eve

        'username': {
            'type': 'string',
            'minlength': 3,
            'maxlength': 32,
            'required': True,
            'unique': True,
        },

        'firstname': {
            'type': 'string',
            'minlength': 1,
            'maxlength': 20,
        },

        'lastname': {
            'type': 'string',
            'minlength': 1,
            'maxlength': 20,
        },

        'email': {
            'type': 'string',
            'minlength': 6,
            'maxlength': 32,
            'required': True,
            'unique': True,
        },

        'pass': {
            'type': 'string',
            'minlength': 6,
            'maxlength': 32,
            'required': True,
        },

        'pic': {
            'type': 'string',
        },

        'links_for_bio': {
            'type': 'string',
            'maxlength': 300,
        },

        'gender': {
            'type': 'string',
        },

        'birthday': {
            'type': 'datetime',
        },

        # 'role': {
        #     #'type': 'list', # тип: список
        #     'type': 'list',
        #     'allowed': ['user', 'someoneelse', 'admin'],
        #     # 'required': True,
        #     'default': 'user',
        # },

        # 'status': {
        #     'type': 'integer',
        #     # 'required': True,
        #     'default': 0,
        # },

        # 'deleted': {
        #     'type': 'integer',
        #     # 'required': True,
        #     'default': 0,
        # },
    },

    'extra_response_fields': ['token'],

    # To hide some secret fields from client, you should use inclusive projection
    'datasource': {
        'projection': {
            'username': 1,
            'firstname': 1,
            'lastname': 1,
            'email': 1,
            'pic': 1,
            'links_for_bio': 1,
            'gender': 1,
            'birthday': 1,
            'role': 1,
            'status': 1,
            'deleted': 1
        }
    },
}


# http://python-eve.org/tutorials/account_management.html
USERS_AUTH = {
    'url': 'users/auth',
    'pagination': False,

    'authentication': AuthByLoginAndPass,

    'additional_lookup': {
        'url': 'regex("[\w]+")',
        'field': 'username',
    },

    'resource_methods': [],
    'public_methods': [],

    'item_methods': ['GET'],
    'public_item_methods': [],

    'schema': {
        'username': {
            'type': 'string',
            'minlength': 3,
            'maxlength': 32,
            'required': True,
            'unique': True,
        },
    },

    'datasource': {
        'source': 'users',
        'projection': {
            'token': 1,

            'username': 0,
            'firstname': 0,
            'lastname': 0,
            'email': 0,
            'pic': 0,
            'links_for_bio': 0,
            'gender': 0,
            'birthday': 0,
            'role': 0,
            'status': 0,
            'deleted': 0,
        }
    }
}

USERS_AUTH_CHECK = {
    'url': 'users/auth/check',
    'pagination': False,

    'additional_lookup': {
        'url': 'regex("[\w]+")',
        'field': 'token',
    },

    'resource_methods': [],
    'public_methods': [],

    'item_methods': ['GET'],
    'public_item_methods': ['GET'],

    'schema': {
        'token': {
            'type': 'string',
            'required': True,
            'unique': True,
        },
    },

    'datasource': {
        'source': 'users',
        'projection': {
            'token': 1,

            'username': 0,
            'firstname': 0,
            'lastname': 0,
            'email': 0,
            'pic': 0,
            'links_for_bio': 0,
            'gender': 0,
            'birthday': 0,
            'role': 0,
            'status': 0,
            'deleted': 0,
        }
    }
}
