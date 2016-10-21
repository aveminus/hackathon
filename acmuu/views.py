from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return HttpResponse("Index.")

def detail(request, repo_name):
    return HttpResponse("You're looking at question %s." % repo_name)

def events(request, repo_name):
    response = "You're looking at the results of question %s."
    return HttpResponse(response % repo_name)

def commits(request, repo_id):
    return HttpResponse("You're voting on question %s." % repo_id)