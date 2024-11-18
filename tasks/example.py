from celery import Task
from tasks import celery_app
import time

@celery_app.task(bind=True)
def add(self, x, y):
    for i in range(5):
        time.sleep(1)
        self.update_state(state='PROGRESS', meta={'progress': (i + 1) * 20})
    return x + y

class MultiplyTask(Task):
    def run(self, x, y):
        for i in range(5):
            time.sleep(1)
            self.update_state(state='PROGRESS', meta={'progress': (i + 1) * 20})
        return x * y

multiplytask = celery_app.register_task(MultiplyTask())