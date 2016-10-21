from django.shortcuts import render
from django.http import HttpResponse
from .models import Repo
from django.shortcuts import get_object_or_404
import json
import urllib2

def index(request):
     return render(request,"acmuu/index.html")
    #return HttpResponse("Index.")

def detail(request, username, repo):
    url = "https://api.github.com/repos/kikofernandez/hackathon/events"
    data = json.load(urllib2.urlopen(url))
    list_details = []
    for i in range(10):
        try:
            detail = data[i]

            type = detail['type']
            time = detail['created_at']
            list_details.append({'type': type,
                                 'time': time
                                 })
        except:
            None
            # print str(list_commits)
    print str(list_details)
    print str(data)
    return render(request, "acmuu/details.html", {'details':list_details})

def user(request, username):
    print username
    return HttpResponse("You're looking at user: %s." % (username))

def events(request, repo_name):
    response = "You're looking at the results of question %s."
    return HttpResponse(response % repo_name)

#
# def commits(request, repo_id):
#     return HttpResponse("You're voting on question %s." % repo_id)