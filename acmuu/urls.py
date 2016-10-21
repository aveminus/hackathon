from django.conf.urls import url

from . import views

urlpatterns = [

    # ex: /acmuu/
    url(r'^$', views.index, name='index'),

    # ex: /acmuu/add/
    url(r'^add/$', views.add_repo, name='add_repo'),

    # # ex: /acmuu/<username>/
    url(r'^(?P<username>[\w-]+)/$', views.user, name='user'),

    # ex: /acmuu/<username>/
    url(r'^(?P<username>[\w-]+)/(?P<repo>[\w-]+)/details/$', views.detail, name='detail'),

    # # ex: /acmuu/<repo-id>/events
    # url(r'^(?P<repo_name>[a-zA-Z\/]+)/events$', views.events, name='events'),

    # ex: /acmuu/<repo-id>/commits
    url(r'^(?P<username>[\w-]+)/(?P<repo>[\w-]+)/commits/$', views.commits, name='commits'),

]