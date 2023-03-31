from django.http import HttpResponse
from django.shortcuts import render
from django.core import serializers

from projects.models import Project

# Create your views here.
def index(request):
    projects = Project.objects.all()
    json = serializers.serialize('json', projects)

    return HttpResponse(json)


def detail(request, project_id):
    return HttpResponse("You're looking at question %s." % project_id)