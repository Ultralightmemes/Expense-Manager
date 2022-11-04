import datetime

from celery import shared_task
from django.conf import settings
from django.core.mail import send_mail
from django.db.models import Sum

from user.models import User


def get_money_per_day(user):
    return user.transaction_set.filter(date_done__gt=datetime.datetime.now() - datetime.timedelta(days=1)).aggregate(
        Sum('sum')).get('sum__sum', 0)


@shared_task
def send_mail_task():
    print("Mail sending.......")
    subject = 'Daily notification'
    email_from = settings.EMAIL_HOST_USER
    users = User.objects.all().prefetch_related('transaction_set')
    for user in users:
        message = f'You have {user.balance} on your balance.\n' \
                  f'Result of Your yesterday transactions {get_money_per_day(user)}'
        send_mail(subject, message, email_from, (user.email,))
    return "Mail has been sent........"
