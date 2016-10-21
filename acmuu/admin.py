from django.contrib import admin
from .models import GitHub, Repo

class RepoAdmin(admin.ModelAdmin):
    list_display = ('repo', 'path')

# Register your models here.
admin.site.register(GitHub)
admin.site.register(Repo, RepoAdmin)