# Описываем ресурс `/users`
USERS = {
    # Здесь мы описываем модель данных. Для валидации используется модуль Cerberus от автора Eve.
    # Вы можете ознакомиться с ним в официальной документации модуля http://docs.python-cerberus.org/en/stable/.
    # Либо прочитать заметки в официальной документации EVE http://python-eve.org/validation.html#validation.
    'schema': {
        # _id added automatically by eve

        'username': {
            'type': 'string',
            'minlength': 3,
            'maxlength': 32,
            'required': True,
            # уникальное поле (индекс не создаётся, просто значение должно быть уникальным)
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
            # уникальное поле (индекс не создаётся, просто значение должно быть уникальным)
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

        # date reg added automatically by eve

        'role': {
            #'type': 'list', # тип: список
            'type': 'integer',
            #'allowed': [0, "author", "contributor"], # разрешаем использовать значения: "author", "contributor"
            'required': True,
            'default': 0,
        },

        'gender': {
            'type': 'string',
        },

        'status': {
            'type': 'integer',
            'required': True,
            'default': 0,
        },

        'deleted': {
            'type': 'integer',
            'required': True,
            'default': 0,
        },

        'birthday': {
            'type': 'datetime',
        },
    },

    'datasource': {
        'projection': {
            'username': 1,
            'firstname': 1,
            'lastname': 1,
            'email': 1,
            'pic': 0,
            'links_for_bio': 1,
            'role': 1,
            'gender': 1,
        }
    },
}
