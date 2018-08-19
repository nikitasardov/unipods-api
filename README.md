**Contents**
- Register user
- Get token
- Get account data
- Useful links
- Modify user`s data by user

**Register user**
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

**Get token**
Endpoint: /users/auth/<username> or /users/auth/<_id>
Method: GET
Returns:
    {
        "_created": "Thu, 01 Jan 1970 00:00:00 GMT",
        "_etag": "25c6a615225e021c70886ab266d7acbcaf23ee88",
        "_id": "5b790c89dbf7245f2f6e1580",
        "_updated": "Thu, 01 Jan 1970 00:00:00 GMT",
        "token": "d9cfbf48bac4e8488ed13d6125572d4ceb5092b6"
    }

Params:
    Header:
        Authorization:Basic dXNlcm5hbWU6MDEyMzQ1Njc4OQ==

    Here 'dXNlcm5hbWU6MDEyMzQ1Njc4OQ==' is base64 encoded string 'username:0123456789'
    Header name is 'Authorization'. Part after ':' is its value

**Get account data**
Endpoint: /users/<username> or /users/<_id>
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
        'token': 1,
        'role': 1,
        'status': 1,
        'deleted': 1
    }

Params:
    Header:
        Authorization: <token>

    Token-based authentication is considered a version of Basic Authentication.
    Header tag contains the auth token as the username, and no password.

**Modify user`s data by user**
Endpoint: /users/<username> or /users/<_id>
Method: PATCH

Params:
    Header:
        Authorization: <token>

    Token-based authentication is considered a version of Basic Authentication.
    Header tag contains the auth token as the username, and no password.

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



**Useful links**
flask
https://www.tutorialspoint.com/flask/flask_quick_guide.htm

flask api
https://auth0.com/blog/developing-restful-apis-with-python-and-flask/
https://habr.com/post/246699/
+TDD https://scotch.io/tutorials/build-a-restful-api-with-flask-the-tdd-way

Полноценный REST API для перфекционистов за 5 минут
https://habr.com/post/276731/

http://python-eve.org/config.html
http://python-eve.org/features.html
http://python-eve.org/authentication.html
http://python-eve.org/validation.html

mongo
https://www.digitalocean.com/community/tutorials/mongodb-ubuntu-16-04-ru
https://docs.mongodb.com/manual/tutorial/enable-authentication/

pgsql
https://www.tutorialspoint.com/postgresql/index.htm
https://www.pgadmin.org/docs/pgadmin4/dev/getting_started.html
https://hub.docker.com/r/dpage/pgadmin4/
http://eve-sqlalchemy.readthedocs.io/en/latest/
https://www.digitalocean.com/community/tutorials/postgresql-ubuntu-16-04-ru

https://blogs.rdoproject.org/2015/07/build-your-restful-api-web-service-in-5-minutes/
