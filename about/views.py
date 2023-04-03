import json
from django.http import HttpResponse
from django.core import serializers

from about.models import Bio, Photo
from django.core.exceptions import ObjectDoesNotExist

def active(request):
    response = {}
    try:
        bio = Bio.objects.get(active=True)
        response['content'] = bio.content
    except ObjectDoesNotExist:
        HttpResponse(status=404)
    
    try:
        photo = Photo.objects.get(active=True)
        response['photo'] = photo.image.name
    except ObjectDoesNotExist:
        HttpResponse(status=404)

    return HttpResponse(json.dumps(response), content_type='application/json')