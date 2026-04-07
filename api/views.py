import random
from django.http import JsonResponse
from .models import CurrentJoke

# Create your views here.

JOKES = [
    "Why don't scientists trust atoms? Because they make up everything.",
    "Did you hear about the mathematician who's afraid of negative numbers? He'll stop at nothing to avoid them.",
    "Why don't skeletons fight each other? They don't have the guts.",
    "What do you call a fake noodle? An impasta.",
    "Why did the scarecrow win an award? Because he was outstanding in his field.",
    "Why did the bicycle fall over? Because it was two-tired.",
    "What do you call cheese that isn't yours? Nacho cheese.",
    "Why did the math book look sad? Because it had too many problems.",
    "What do you call a snowman with a six-pack? An abdominal snowman.",
    "I told my doctor that I broke my arm in two places. He told me to stop going to those places."
]

def random_joke(request):
    try:
        joke_obj = CurrentJoke.objects.get(id=1)
        joke = joke_obj.text
    except CurrentJoke.DoesNotExist:
        joke = "No jokes are available yet! The backend is sleeping."
    response = JsonResponse({"joke": joke})
    # Setting wrong security headers for testing purposes
    response['X-Content-Type-Options'] = 'wrong-value'
    response['Content-Security-Policy'] = 'default-src wrong-value;'
    response['Strict-Transport-Security'] = 'max-age=wrong-value'
    return response
