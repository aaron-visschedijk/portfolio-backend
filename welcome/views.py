import json
from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def index(request):
    return HttpResponse(json.dumps("The portfolio backend api is live!"))