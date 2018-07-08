# Описываем ресурс `/stars`
STARS = {
    # Здесь мы описываем модель данных. Для валидации используется модуль Cerberus от автора Eve.
    # Вы можете ознакомиться с ним в официальной документации модуля http://docs.python-cerberus.org/en/stable/.
    # Либо прочитать заметки в официальной документации EVE http://python-eve.org/validation.html#validation.
    'schema': {
        # _id added automatically by eve

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
    }
}