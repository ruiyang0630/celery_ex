from .model import api
from flask_restx import Resource
from apis.model import *
from tasks.example import add, multiplytask
from celery.result import AsyncResult
from tasks import celery_app

@api.route('/celery_task/')
class PostTask(Resource):    
    @api.expect(add_input_payload)
    def post(self):
        data = api.payload
        task = add.delay(data['num1'], data['num2'])
        return {'task_id': task.id}, 200
    
@api.route('/celery_task/<int:num1>/<int:num2>')
class GetTask(Resource):
    def get(self, num1, num2):
        task = multiplytask.delay(num1, num2)
        return {'task_id': task.id}, 200

@api.route('/status/<string:task_id>')
class TaskStatus(Resource):
    def get(self, task_id):
        task = AsyncResult(task_id, app=celery_app)
        if task.state == 'PENDING':
            return {'state': 'PENDING'}
        
        elif task.state == 'PROGRESS':
            try:
                progress = task.info.get('progress', 0)
            except:
                progress = 0
            return {'state': 'PROGRESS', 'progress': progress}
        
        elif task.state == 'SUCCESS' or task.state == 'FAILURE':
            return {'state': task.state, 'result': task.result}