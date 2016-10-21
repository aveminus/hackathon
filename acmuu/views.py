from django.shortcuts import render
from django.http import HttpResponse
from .models import Repo
from django.shortcuts import get_object_or_404

def index(request):

    return HttpResponse("Index.")

def detail(request, username, repo):
    repo = get_object_or_404(Repo, path="%s/%s" % (username, repo))
    return HttpResponse("You're looking at user: %s, %s." % (username, repo.path))

def user(request, username):
    print username
    return HttpResponse("You're looking at user: %s." % (username))

def events(request, repo_name):
    response = "You're looking at the results of question %s."
    return HttpResponse(response % repo_name)

#
# def commits(request, repo_id):
#     return HttpResponse("You're voting on question %s." % repo_id)