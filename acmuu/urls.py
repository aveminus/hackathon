from django.conf.urls import url

from . import views

urlpatterns = [

    # ex: /acmuu/
    url(r'^$', views.index, name='index'),

    # ex: /acmuu/<repo-id>/
    url(r'^(?P<user>[\w]+)/(?P<repo>)$', views.detail, name='detail'),

    # # ex: /acmuu/<repo-id>/events
    # url(r'^(?P<repo_name>[a-zA-Z\/]+)/events$', views.events, name='events'),
    #
    # # ex: /acmuu/<repo-id>/commits
    # url(r'^(?P<repo_name>[0-9]+)/commits$', views.commits, name='commits'),

]