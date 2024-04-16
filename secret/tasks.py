from datetime import datetime, timedelta
import pytz

from celery import shared_task

from secret.models import Secret


@shared_task
def delete_open_secret() -> None:
    """
    Shared task for Celery. Check and collect 'open' secrets then delete them from DB.
    :return:
    Delete 'open' Secrets
    """
    secrets_set = Secret.objects.filter(is_open=True).all()
    for secret in secrets_set:
        secret.delete()


@shared_task
def delete_secret_for_end_time() -> None:
    """
    Shared task for Celery. Check 'lifetime' of Secrets and then delete 'outdated' Secrets from DB.
    :return:
    Delete 'outdated' Secrets
    """
    secrets_set = Secret.objects.all()
    local_tz = pytz.timezone('Europe/Minsk')
    time_now = datetime.now()
    local_time = time_now.replace(tzinfo=pytz.utc).astimezone(local_tz)
    for secret in secrets_set:
        if secret.lifetime == '30_min':
            delta = timedelta(minutes=30)
            if local_time - secret.created_at > delta:
                secret.delete()
        elif secret.lifetime == '1_hour':
            delta = timedelta(hours=1)
            if local_time - secret.created_at > delta:
                secret.delete()
        elif secret.lifetime == '4_hour':
            delta = timedelta(hours=4)
            if local_time - secret.created_at > delta:
                secret.delete()
        elif secret.lifetime == '12_hour':
            delta = timedelta(hours=12)
            if local_time - secret.created_at > delta:
                secret.delete()
        elif secret.lifetime == '1_day':
            delta = timedelta(days=1)
            if local_time - secret.created_at > delta:
                secret.delete()
        elif secret.lifetime == '7_day':
            delta = timedelta(days=7)
            if local_time - secret.created_at > delta:
                secret.delete()
