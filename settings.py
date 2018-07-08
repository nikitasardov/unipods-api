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

from resources.users import USERS
from resources.podcasts import PODCASTS
from resources.comments import COMMENTS
from resources.stars import STARS
from resources.categories import CATEGORIES

# замените user, password, ds049945.mongolab.com, example на ваши данные доступа к БД.
MONGO_URI = "mongodb://127.0.0.1:27017/" + APP_DB

# По умолчанию Eve запускает API в режиме "read-only" (т.е. поддерживаются только GET запросы),
# мы включаем поддержку методов POST, PUT, PATCH, DELETE.
RESOURCE_METHODS = ['GET', 'POST']
ITEM_METHODS = ['GET', 'PATCH', 'PUT', 'DELETE']

# describing resourses
DOMAIN = {
    'users': USERS,

    'podcasts': PODCASTS,

    'comments': COMMENTS,

    'stars': STARS,

    'categories': CATEGORIES,
}