### Contents
- Register user
- Get token
- Get account data
- Modify user`s data by user
- Check token
- Useful links

### Register user
Endpoint: /users

Method: POST

Returns:

	{
        "_created": "Sun, 19 Aug 2018 10:56:25 GMT",
        "_etag": "3562c131d49afdc73f91a2cf92b62f21b45ea73b",
        "_id": "5b794cd9dbf7246ab5472abd",
        "_status": "OK",
        "_updated": "Sun, 19 Aug 2018 10:56:25 GMT",
        "token": "99aefb5f1d4dd49702079826b181d7e5684ac916"
    }

Params:

    Header:
        Content-Type:application/json

    'username': {
        'type': 'string',
        'minlength': 3,
        'maxlength': 32,
        **'required': True,**
        **'unique': True,**
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
        **'required': True,**
        **'unique': True,**
    },

    'pass': {
        'type': 'string',
        'minlength': 6,
        'maxlength': 32,
        **'required': True,**
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
    }

### Get token
Endpoint: /users/auth/\<username> or /users/auth/\<_id>

Method: GET

Returns:

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

Params:

    Header:
        Authorization: Basic dXNlcm5hbWU6MDEyMzQ1Njc4OQ==

Here 'dXNlcm5hbWU6MDEyMzQ1Njc4OQ==' is base64 encoded string '\<username>:\<pass>'.
Header name is 'Authorization'. Its value follows after ':'.

### Get account data
Endpoint: /users/\<username> or /users/\<_id>

Method: GET

Returns:

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

In eve projection defines available fields of response. Pass and token are not included here.

Params:

    Header:
        Authorization: <token>

Token-based authentication is considered a version of Basic Authentication.
Authorization header contains the auth token as the username, and no password.

### Modify user\`s data by user
Endpoint: /users/\<_id>

    This endpoint /users/\<username> is not available for PATCH.
    Use item <_id> with PATCH method.

Method: PATCH

Params:

    Headers:
        Authorization: <token>
        If-Match: <_etag>

Token-based authentication is considered a version of Basic Authentication.
Authorization header contains the auth token as the username, and no password.

If-Match header should contain proper _etag, otherwise you'll get error 412 "Precondition failed" or 428 for absent If-Match

    'username',
    'firstname',
    'lastname',
    'email',
    'pass',
    'pic',
    'links_for_bio',
    'gender',
    'birthday'

See list of available fields with descriptions in "Register user"

### Check token
Endpoint: /users/auth/check/\<token>

Method: GET

Returns:

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

In eve projection defines available fields of response. Pass is not included here.

Params:

    no params


### Useful links
##### flask
https://www.tutorialspoint.com/flask/flask_quick_guide.htm

##### flask api
https://auth0.com/blog/developing-restful-apis-with-python-and-flask/

https://habr.com/post/246699/

+TDD https://scotch.io/tutorials/build-a-restful-api-with-flask-the-tdd-way

##### Полноценный REST API для перфекционистов за 5 минут
https://habr.com/post/276731/

##### Python Eve
http://python-eve.org/config.html

http://python-eve.org/features.html

http://python-eve.org/authentication.html

http://python-eve.org/validation.html

##### mongo
https://www.digitalocean.com/community/tutorials/mongodb-ubuntu-16-04-ru

https://docs.mongodb.com/manual/tutorial/enable-authentication/

##### pgsql
https://www.tutorialspoint.com/postgresql/index.htm

https://www.pgadmin.org/docs/pgadmin4/dev/getting_started.html

https://hub.docker.com/r/dpage/pgadmin4/

http://eve-sqlalchemy.readthedocs.io/en/latest/

https://www.digitalocean.com/community/tutorials/postgresql-ubuntu-16-04-ru

##### RESTful api
https://blogs.rdoproject.org/2015/07/build-your-restful-api-web-service-in-5-minutes/
