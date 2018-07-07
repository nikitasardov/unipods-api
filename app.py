# Полноценный REST API для перфекционистов за 5 минут
# https://habr.com/post/276731/

# http://python-eve.org/features.html

# https://www.digitalocean.com/community/tutorials/mongodb-ubuntu-16-04-ru

try:
    from env_config import *
except ImportError:
    with open('env_config.py', 'w', encoding='utf-8') as f:
        f.write("APP_PORT = 4507\nAPP_ENV = 'dev'\nAPP_DEBUG = True")
        f.close()

    print('Default dev vars initialized, dev config written to env_config.py')
    APP_PORT = 4507
    APP_ENV = 'dev'
    APP_DEBUG = True

from eve import Eve
app = Eve()


@app.after_request
def cors_headers(response):
    response.headers['Access-Control-Allow-Origin'] = '*'
    response.headers['Access-Control-Allow-Headers'] = 'Content-Type'
    response.headers['Access-Control-Allow-Methods'] = 'GET, OPTIONS, PUT'
    response.headers['Content-Type'] = 'application/json; charset=utf-8'

    return response
if __name__ == '__main__':
    app.debug = APP_DEBUG
    app.run(host='0.0.0.0', port=APP_PORT)