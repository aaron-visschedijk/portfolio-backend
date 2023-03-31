from django.http import HttpResponse
from django.core import serializers

from about.models import Bio, Photo

def active(request):
    bio = Bio.objects.get(active=True)
    photo = Photo.objects.get(active=True)
    json = serializers.serialize('json', [bio, photo])
    return HttpResponse(json, content_type='application/json')