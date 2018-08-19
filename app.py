# -*- coding: utf-8 -*-

try:
    from env_config import *
except ImportError:
    with open('env_config.py', 'w', encoding='utf-8') as f:
        f.write("APP_PORT = 4507\nAPP_ENV = 'dev'\nAPP_DEBUG = True\nAPP_DB = APP_ENV + '_unipods'")
        f.close()

    print('Default dev vars initialized, dev config written to env_config.py')
    APP_PORT = 4507
    APP_ENV = 'dev'
    APP_DEBUG = True
    APP_DB = APP_ENV + '_unipods'

from eve import Eve
from eve.auth import TokenAuth
import resources as res

print('====> Using db "{}" <===='.format(APP_DB))

# @app.after_request
# def cors_headers(response):
#     response.headers['Access-Control-Allow-Origin'] = '*'
#     response.headers['Access-Control-Allow-Headers'] = 'Content-Type'
#     response.headers['Access-Control-Allow-Methods'] = 'GET, OPTIONS, PUT'
#     response.headers['Content-Type'] = 'application/json; charset=utf-8'
#     return response


class AuthByToken(TokenAuth):
    def check_auth(self, token, allowed_roles, resource, method):
        # use Eve's own db driver; no additional connections/resources are used
        users = app.data.driver.db['users']
        lookup = {'token': token}
        # if allowed_roles:
        #     # only retrieve a user if his roles match ``allowed_roles``
        #     lookup['roles'] = {'$in': allowed_roles}
        user = users.find_one(lookup)
        return user

if __name__ == '__main__':
    app = Eve(auth=AuthByToken)
    app.on_insert_users += res.users.add_user_defaults
    app.debug = APP_DEBUG
    app.run(host='0.0.0.0', port=APP_PORT)
