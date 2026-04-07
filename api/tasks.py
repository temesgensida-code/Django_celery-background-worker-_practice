from celery import shared_task
import random
from .models import CurrentJoke
from .views import JOKES

@shared_task
def update_joke():
    joke_text = random.choice(JOKES)
    joke_obj, created = CurrentJoke.objects.get_or_create(id=1, defaults={"text": joke_text})
    if not created:
        joke_obj.text = joke_text
        joke_obj.save()
    return joke_text
