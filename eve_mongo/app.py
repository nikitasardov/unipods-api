# Полноценный REST API для перфекционистов за 5 минут
# https://habr.com/post/276731/

# http://python-eve.org/features.html

# https://www.digitalocean.com/community/tutorials/mongodb-ubuntu-16-04-ru

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
    app.run()