# Описываем ресурс `/comments`
COMMENTS = {
    # Здесь мы описываем модель данных. Для валидации используется модуль Cerberus от автора Eve.
    # Вы можете ознакомиться с ним в официальной документации модуля http://docs.python-cerberus.org/en/stable/.
    # Либо прочитать заметки в официальной документации EVE http://python-eve.org/validation.html#validation.
    'schema': {
        # _id added automatically by eve

        'parent_id': {
            'type': 'string',
            'maxlength': 100,
        },

        'user_id': {
            'type': 'string',
            'maxlength': 100,
            'required': True,
        },

        'podcast_id': {
            'type': 'string',
            'maxlength': 100,
            'required': True,
        },

        # date reg added automatically by eve

        'content': {
            'type': 'string',
            'maxlength': 500,
            'required': True,
        },

        'like': {
            'type': 'integer',
        },

        'dislike': {
            'type': 'integer',
        },

        'deleted': {
            'type': 'integer',
            'required': True,
            'default': 0
        },
    }
}