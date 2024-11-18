from celery import Celery

celery_app = Celery(__name__, 
                    broker='redis://redis:6379/0', 
                    backend='redis://redis:6379/1'
)
celery_app.conf.update({
    'imports': ('tasks.example',),
    'result_serializer': 'json',
})
