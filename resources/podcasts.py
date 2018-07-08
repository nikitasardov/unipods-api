# Описываем ресурс `/podcasts`
PODCASTS = {
    # Здесь мы описываем модель данных. Для валидации используется модуль Cerberus от автора Eve.
    # Вы можете ознакомиться с ним в официальной документации модуля http://docs.python-cerberus.org/en/stable/.
    # Либо прочитать заметки в официальной документации EVE http://python-eve.org/validation.html#validation.
    'schema': {
        # _id added automatically by eve

        'title': {
            'type': 'string',
            'minlength': 3,
            'maxlength': 100,
            'required': True,
        },

        'descr': {
            'type': 'string',
            'maxlength': 400,
        },

        'pic': {
            'type': 'string',
        },

        'links': {
            'type': 'string',
            'maxlength': 300,
        },

        'lang': {
            'type': 'string',
            'minlength': 2,
            'maxlength': 32,
            'required': True,
        },

        'release_per_week_month': {
            'type': 'string',
            'default': '0',
        },

        'total_stars': {
            'type': 'string',
            'maxlength': 10
        },

        'publish': {
            'type': 'integer',
            'required': True,
            'default': 0
        },

        'status': {
            'type': 'integer',
            'required': True,
            'default': 0
        },

        'cat': {
            'type': 'string',
            'maxlength': 30
        },
    }
}