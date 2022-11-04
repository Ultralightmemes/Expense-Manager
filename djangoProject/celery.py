from __future__ import absolute_import, unicode_literals
import os
from celery import Celery
from django.apps import apps
from celery.schedules import crontab

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'djangoProject.settings')
app = Celery('djangoProject')
app.conf.enable_utc = False
app.conf.update(timezone='Europe/Minsk')
app.config_from_object('django.conf:settings', namespace='')
app.conf.beat_schedule = {
    'Send_mail_to_Client': {
        'task': 'user.tasks.send_mail_task',
        # 'schedule': crontab(minute=0, hour='8')
        'schedule': 30
    }
}
app.autodiscover_tasks(lambda: [n.name for n in apps.get_app_configs()])


@app.task(bind=True)
def debug_task(self):
    print(f'Request: {self.request!r}')
