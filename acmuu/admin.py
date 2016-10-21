from django.contrib import admin
from .models import GitHub, Repo

# Register your models here.
admin.site.register(GitHub)
admin.site.register(Repo)