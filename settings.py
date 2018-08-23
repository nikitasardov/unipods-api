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

import resources as res

# http://python-eve.org/config.html

URL_PREFIX = ''
API_VERSION = ''

ALLOWED_FILTERS = []
VALIDATE_FILTERS = False
SORTING = True

PAGINATION = True
PAGINATION_LIMIT = 50
PAGINATION_DEFAULT = 25
OPTIMIZE_PAGINATION_FOR_SPEED = False

QUERY_WHERE = 'where'
QUERY_SORT = 'sort'
QUERY_PROJECTION = 'projection'
QUERY_PAGE = 'page'
QUERY_MAX_RESULTS = 'max_results'
QUERY_EMBEDDED = 'embedded'
QUERY_AGGREGATION = 'aggregate'

# DATE_FORMAT = 'a, %d %b %Y %H:%M:%S GMT'

# По умолчанию Eve запускает API в режиме "read-only" (т.е. поддерживаются только GET запросы),
# мы включаем поддержку методов POST, PUT, PATCH, DELETE.
RESOURCE_METHODS = ['GET', 'POST']
PUBLIC_METHODS = ['GET']
ITEM_METHODS = ['GET', 'PATCH', 'DELETE']
PUBLIC_ITEM_METHODS = ['GET']

ALLOWED_ROLES = ['admin']
ALLOWED_READ_ROLES = ['admin']
ALLOWED_WRITE_ROLES = ['admin']
ALLOWED_ITEM_ROLES = ['admin']
ALLOWED_ITEM_READ_ROLES = ['admin']
ALLOWED_ITEM_WRITE_ROLES = ['admin']

ALLOW_OVERRIDE_HTTP_METHOD = True

# CACHE CONTROL
CACHE_CONTROL = 'private,max-age=0,no-cache'
CACHE_EXPIRES = 0

# CORS
if APP_ENV == 'prod':
    X_DOMAINS = ['unipods.ru']
else:
    X_DOMAINS = ['*']
X_DOMAINS_RE = None

X_HEADERS = ['Content-Type', 'Authorization']
X_EXPOSE_HEADERS = None
X_ALLOW_CREDENTIALS = True
X_MAX_AGE = 21600

# '_updated'
# LAST_UPDATED
# '_created'
# DATE_CREATED
# '_id'
# ID_FIELD

# ITEM_LOOKUP
# ITEM_LOOKUP_FIELD

# ITEM_URL = regex("[a-f0-9]{24}")
# ITEM_TITLE

# AUTH_FIELD
ALLOW_UNKNOWN = False

PROJECTION = True
EMBEDDING = True

BANDWIDTH_SAVER = True
# EXTRA_RESPONSE_FIELDS = []

RATE_LIMIT_GET = None
RATE_LIMIT_POST = None
RATE_LIMIT_PATCH = None
RATE_LIMIT_DELETE = None

# DEBUG

# '_error'
# ERROR

HATEOAS = False

# '_issues'
# ISSUES
# '_status'
# STATUS
STATUS_OK = 'OK'
STATUS_ERR = 'ERR'

# '_items'
# ITEMS
# '_meta'
# META

INFO = None

# '_links'
# LINKS
# '_etag'
# ETAG

IF_MATCH = True
ENFORCE_IF_MATCH = True

RENDERERS = [
    'eve.render.JSONRenderer',
    # 'eve.render.XMLRenderer'
]

JSON_SORT_KEYS = True
JSON_REQUEST_CONTENT_TYPES = ['application/json']

VALIDATION_ERROR_STATUS = 422

VERSIONING = False
# VERSIONS = '_versions'
# VERSION_PARAM = 'version'
# VERSION = '_version'
# LATEST_VERSION = '_latest_version'
# VERSION_ID_SUFFIX = '_document'


# MONGO_URI = "mongodb://127.0.0.1:27017/" + APP_DB
MONGO_HOST = 'localhost'
MONGO_PORT = 27017
# MONGO_USERNAME = 'user'
# MONGO_PASSWORD = 'user'
MONGO_DBNAME = APP_DB
MONGO_OPTIONS = {'connect': True, 'tz_aware': True, 'appname': 'flask_app_name'}
MONGO_AUTH_SOURCE = None
MONGO_AUTH_MECHANISM = None
MONGO_AUTH_MECHANISM_PROPERTIES = None
MONGO_QUERY_BLACKLIST = ['$where', '$regex']
MONGO_WRITE_CONCERN = {'w': 1}

# ALLOW_UNKNOWN = False

# describing resourses
DOMAIN = {
    'users': res.users.USERS,
    'users_auth': res.users.USERS_AUTH,
    'users_auth_check': res.users.USERS_AUTH_CHECK,
    'categories': res.CATEGORIES,
    'podcasts': res.PODCASTS,
    'comments': res.COMMENTS,
    'stars': res.STARS,
}

# EXTENDED_MEDIA_INFO
RETURN_MEDIA_AS_BASE64_STRING = True
RETURN_MEDIA_AS_URL = False
MEDIA_BASE_URL = None
MEDIA_ENDPOINT = 'media'
# MEDIA_URL = regex("[a-f0-9]{24}")

MULTIPART_FORM_FIELDS_AS_JSON = True
AUTO_COLLAPSE_MULTI_KEYS = True
AUTO_CREATE_LISTS = True

OPLOG = False
OPLOG_NAME = 'oplog'
OPLOG_METHODS = ['DELETE', 'POST', 'PATCH', 'PUT']
OPLOG_CHANGE_METHODS = ['DELETE', 'PATCH', 'PUT']
OPLOG_ENDPOINT = None
OPLOG_AUDIT = True
OPLOG_RETURN_EXTRA_FIELD = False

SCHEMA_ENDPOINT = None

HEADER_TOTAL_COUNT = 'X-Total-Count'

JSONP_ARGUMENT = None

BULK_ENABLED = False
SOFT_DELETE = False

# '_deleted'
# DELETED
SHOW_DELETED_PARAM = 'show_deleted'

STANDARD_ERRORS = [400, 401, 403, 404, 405, 406, 409, 410, 412, 422, 428]

VALIDATION_ERROR_AS_STRING = True

UPSERT_ON_PUT = False

MERGE_NESTED_DOCUMENTS = True
