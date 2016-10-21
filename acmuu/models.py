from __future__ import unicode_literals

from django.db import models


# Create your models here.
#
class GitHub(models.Model):
    username = models.CharField(max_length=200)
    password = models.CharField(max_length=100)
    # user = models.ForeignKey(models.User)

class Repo(models.Model):
    REPOCHOICE = (
        ('g', 'GitHub'),
        ('b', 'Bitbucket'),
        ('gl', 'Gitlab'),
    )

    repo = models.CharField(max_length=2, choices=REPOCHOICE)
    path = models.CharField(max_length=100, help_text="username/project")


