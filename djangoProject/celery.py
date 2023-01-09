import os

import dotenv
from celery import Celery
from celery.schedules import crontab

env_file = os.path.join(os.path.dirname(os.path.dirname(os.path.realpath(__file__))), '.env')
dotenv.read_dotenv(env_file)

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'djangoProject.settings')
app = Celery('djangoProject')

app.config_from_object('django.conf:settings', namespace='')

app.conf.beat_schedule = {
    'Send_mail_to_Client': {
        'task': 'user.tasks.send_mail_task',
        # 'schedule': crontab(minute=0, hour='8')
        'schedule': 30
    }
}
app.autodiscover_tasks()


# @app.task(bind=True)
# def debug_task(self):
#     print(f'Request: {self.request!r}')
