from celery import shared_task
from django.utils import timezone
from .models import Subscription
import logging

logger = logging.getLogger(__name__)

@shared_task
def cancel_expired_subscriptions():
    expired_subs = Subscription.objects.filter(
        is_active=True, 
        end_date__lt=timezone.now()
    )
    count = expired_subs.update(is_active=False)
    logger.info(f"{count} ta muddati o'tgan obunalar avtomatik bekor qilindi.")