from flask import Flask
from flask_restx import Api
from apis.api import api as tasks_ns

app = Flask(__name__)
api = Api(app, version='1.0', title='Celery', doc='/api')
api.add_namespace(tasks_ns, path='')

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=80)