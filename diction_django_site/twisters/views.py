from django.http import JsonResponse
from diction_django_site.twisters.models import Twister
import random

def twisters(request):
    twisters = [twister for twister in Twister.objects.all().values_list('twister', 'source')]
    return JsonResponse({'twisters': twisters})

def twister(request):
    twisters = [twister for twister in Twister.objects.all().values_list('twister', 'source')]
    random_twister = random.choice(twisters)
    return JsonResponse({'twister': random_twister[0], 'source': random_twister[1]})