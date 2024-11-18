from flask_restx import fields, Namespace

api = Namespace("tasks", description=u"celery練習")

add_input_payload = api.model(u'加法輸入參數定義', {
    'num1': fields.Integer(required=True, default=6),
    'num2': fields.Integer(required=True, default=6),
})