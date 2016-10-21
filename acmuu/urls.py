from django.conf.urls import url

from . import views

urlpatterns = [

    # ex: /acmuu/
    url(r'^$', views.index, name='index'),

    # # ex: /acmuu/<username>/
    url(r'^(?P<username>[\w-]+)/$', views.user, name='user'),

    # ex: /acmuu/<username>/
    url(r'^(?P<username>[\w-]+)/(?P<repo>[\w-]+)/$', views.detail, name='detail'),

    # # ex: /acmuu/<repo-id>/events
    # url(r'^(?P<repo_name>[a-zA-Z\/]+)/events$', views.events, name='events'),
    #
    # # ex: /acmuu/<repo-id>/commits
    # url(r'^(?P<repo_name>[0-9]+)/commits$', views.commits, name='commits'),

]