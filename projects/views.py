import json
from django.http import HttpResponse
from django.shortcuts import render
from django.core import serializers
from django.core.exceptions import ObjectDoesNotExist

from projects.models import Project

# Create your views here.


def index(request):
    response = []

    projects = Project.objects.all()

    for project in projects:
        if project.hidden:
            continue

        tags = [{'name': tag.name, 'color': tag.color}
                for tag in project.tags.all()]

        response.append({
            'id': project.pk,
            'title': project.title,
            'titleLong': project.title_long,
            'description': project.description,
            'image': project.image.name,
            'date': project.date.strftime('%Y-%m-%d'),
            'link': project.link,
            'linkText': project.link_text,
            'github': project.github,
            'tags': tags,
        })

    return HttpResponse(json.dumps(response), content_type='application/json')