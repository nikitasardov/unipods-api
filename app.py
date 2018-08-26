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

from flask import current_app as capp
from flask_admin import Admin
from flask_admin.contrib.pymongo import ModelView, filters

from wtforms import form, fields
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


# Users admin
class InnerForm(form.Form):
    name = fields.StringField('Name')
    test = fields.StringField('Test')


class UsersForm(form.Form):
    login = fields.StringField('login')
    fullname = fields.StringField('fullname')
    email = fields.StringField('email')
    passw = fields.StringField('pass')
    pic = fields.StringField('pic')
    links_for_bio = fields.StringField('links_for_bio')
    gender = fields.StringField('gender')
    birthday = fields.StringField('birthday')
    role = fields.StringField('role')
    status = fields.StringField('status')
    deleted = fields.StringField('deleted')


class UsersView(ModelView):
    column_list = ('login', 'fullname', 'email', 'pass', 'pic', 'links_for_bio', 'gender',
                   'birthday', 'role', 'status', 'deleted')
    column_sortable_list = ('login', 'fullname', 'email', 'pass', 'pic', 'links_for_bio', 'gender',
                            'birthday', 'role', 'status', 'deleted')

    form = UsersForm


# Podcasts admin
class PodcastsForm(form.Form):
    title = fields.StringField('title')
    descr = fields.StringField('descr')
    pic = fields.StringField('pic')
    links = fields.StringField('links')
    lang = fields.StringField('lang')
    release_per_week_month = fields.StringField('release_per_week_month')
    total_stars = fields.StringField('total_stars')
    publish = fields.StringField('publish')
    status = fields.StringField('status')
    cat = fields.StringField('cat')


class PodcastsView(ModelView):
    column_list = ('title', 'descr', 'pic', 'links', 'lang', 'release_per_week_month', 'total_stars', 'publish',
                   'status', 'cat')
    column_sortable_list = ('title', 'descr', 'pic', 'links', 'lang', 'release_per_week_month', 'total_stars', 'publish',
                            'status', 'cat')

    form = PodcastsForm


# Categories admin
class CategoriesForm(form.Form):
    user_id = fields.StringField('user_id')
    podcast_id = fields.StringField('podcast_id')


class CategoriesView(ModelView):
    column_list = ('user_id', 'podcast_id')
    column_sortable_list = ('user_id', 'podcast_id')

    form = CategoriesForm


# Comments admin
class CommentsForm(form.Form):
    parent_id = fields.StringField('parent_id')
    user_id = fields.StringField('user_id')
    podcast_id = fields.StringField('podcast_id')
    content = fields.StringField('content')
    like = fields.StringField('like')
    dislike = fields.StringField('dislike')
    deleted = fields.StringField('deleted')


class CommentsView(ModelView):
    column_list = ('parent_id', 'user_id', 'podcast_id', 'content', 'like', 'dislike', 'deleted')
    column_sortable_list = ('parent_id', 'user_id', 'podcast_id', 'content', 'like', 'dislike', 'deleted')

    form = CommentsForm


# Stars admin
class StarsForm(form.Form):
    user_id = fields.StringField('user_id')
    podcast_id = fields.StringField('podcast_id')


class StarsView(ModelView):
    column_list = ('user_id', 'podcast_id')
    column_sortable_list = ('user_id', 'podcast_id')

    form = StarsForm

if __name__ == '__main__':
    app = Eve(auth=AuthByToken)
    app.secret_key = '38fjryuf7' + APP_ENV + 'drhsr47vdv'
    admin = Admin(app, name='unipods ' + APP_ENV, template_mode='bootstrap3')
    with app.app_context():
        # within this block, current_app points to app.
        admin.add_view(UsersView(capp.data.driver.db['users']))
        admin.add_view(PodcastsView(capp.data.driver.db['podcasts']))
        admin.add_view(CategoriesView(capp.data.driver.db['categories']))
        admin.add_view(CommentsView(capp.data.driver.db['comments']))
        admin.add_view(StarsView(capp.data.driver.db['stars']))

    app.on_insert_users += res.users.add_user_defaults
    app.debug = APP_DEBUG
    app.run(host='0.0.0.0', port=APP_PORT)
