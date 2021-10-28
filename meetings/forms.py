from django.contrib.auth.models import User
from django.forms import ModelForm
from django import forms

from meetings.models import Meeting, Organizer, MeetingRoom


class MeetingAddForm(ModelForm):
    class Meta:
        model = Meeting
        fields = ['organizer', 'date', 'visitors', 'meeting_room', 'note']


class OrganizerAddForm(ModelForm):
    class Meta:
        model = Organizer
        fields = ['user', 'department']

class MeetingSearchForm(forms.Form):
    organizer = forms.CharField(required=False)
    date_from = forms.DateField(required=False)
    date_to = forms.DateField(required=False)
    visitors = forms.CharField(required=False)
    visiting_company = forms.CharField(required=False)
    meeting_room = forms.CharField(required=False)
