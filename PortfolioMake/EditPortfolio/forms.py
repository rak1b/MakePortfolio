from django import forms
from froala_editor.widgets import FroalaEditor
from .models import projectsModel
class editorForm(forms.ModelForm):
  class Meta:
    model = projectsModel
    fields = ["full_description"]
  # content = forms.CharField(widget=FroalaEditor)