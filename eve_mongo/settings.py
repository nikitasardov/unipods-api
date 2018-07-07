# замените user, password, ds049945.mongolab.com, example на ваши данные доступа к БД.
MONGO_URI = "mongodb://127.0.0.1:27017/dev_unipods"

# По умолчанию Eve запускает API в режиме "read-only" (т.е. поддерживаются только GET запросы),
# мы включаем поддержку методов POST, PUT, PATCH, DELETE.
#RESOURCE_METHODS = ['GET', 'POST', 'DELETE']
RESOURCE_METHODS = ['GET', 'POST']
ITEM_METHODS = ['GET', 'PATCH', 'PUT', 'DELETE']

DOMAIN = {
    # Описываем ресурс `/users`
    'users': {
        # Здесь мы описываем модель данных. Для валидации используется модуль Cerberus от автора Eve.
        # Вы можете ознакомиться с ним в официальной документации модуля http://docs.python-cerberus.org/en/stable/.
        # Либо прочитать заметки в официальной документации EVE http://python-eve.org/validation.html#validation.
        'schema': {
            # id added automatically by eve
            'username': {
                'type': 'string',
                'minlength': 3,
                'maxlength': 32,
                'required': True,
                # уникальное поле (индекс не создаётся, просто значение должно быть уникальным)
                'unique': True,
            },
            # 'firstname': {
            #     'type': 'string',
            #     'minlength': 1,
            #     'maxlength': 20,
            #     'required': False,
            # },
            # 'lastname': {
            #     'type': 'string',
            #     'minlength': 1,
            #     'maxlength': 20,
            #     'required': False,
            # },
            'email': {
                'type': 'string',
                'minlength': 6,
                'maxlength': 32,
                'required': True,
                # уникальное поле (индекс не создаётся, просто значение должно быть уникальным)
                'unique': True,
            },
            'pass': {
                'type': 'string',
                'minlength': 6,
                'maxlength': 32,
                'required': True,
            },
            # pic(!req)
            # links for bio (!req)
            # date reg added automatically by eve
            'role': {
                #'type': 'list', # тип: список
                'type': 'integer',
                #'allowed': [0, "author", "contributor"], # разрешаем использовать значения: "author", "contributor"
                'required': True,
                'default': 0,
            },
            # gender (!req)
            'status': {
                'type': 'integer',
                'required': True,
                'default': 0
            },
            'deleted': {
                'type': 'integer',
                'required': True,
                'default': 0
            },
            # 'birthday': {
            #     'required': False,
            #     'type': 'datetime',
            # },
            # 'location': {
            #     'type': 'dict', # тип: словарь
            #     # описываем "схему" словаря
            #     'schema': {
            #         'address': {'type': 'string'},
            #         'city': {'type': 'string'}
            #     },
            # },
        }
    },

    # Описываем ресурс `/groups`
    'groups': {
        # Описываем модель данных (см. выше).
        'schema': {
            'title': {
                'type': 'string',
                'minlength': 5,
                'maxlength': 32,
                'required': True,
                'unique': True
            },
            'users': {
                'type': 'list',  # тип: список
                'default': [],   # по умолчанию: пустой список
                # описываем "схему" списка
                'schema': {
                    'type': 'objectid', # тип данных: objectid
                    # ссылаемся на запись в другой коллекции
                    'data_relation': {
                        'resource': 'users',  # на ресурс `users` (который мы описали выше)
                        'field': '_id',  # на поле `_id`
                        'embeddable': True
                    }
                }
            }
        }
    }


}