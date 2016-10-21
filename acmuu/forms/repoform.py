from django.forms import ModelForm
from acmuu.models import Repo

class RepoForm(ModelForm):
    class Meta:
        model = Repo
        fields = ['repo', 'path']