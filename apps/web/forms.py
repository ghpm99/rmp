from django import forms

from web.models import Youtube


class SendVideoForm(forms.Form):
    class Meta:
        model = Youtube
        fields = ['url_path']
