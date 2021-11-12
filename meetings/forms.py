from django.contrib.auth.models import User
from django.forms import ModelForm
from django import forms

from meetings.models import Meeting, Organizer, MeetingRoom
from visitors.models import Company, Visitor


class MeetingAddForm(ModelForm):
    class Meta:
        model = Meeting
        fields = ['organizer', 'date', 'visitors', 'meeting_room', 'note']
        widgets = {'date': forms.widgets.SelectDateWidget}


class OrganizerAddForm(ModelForm):
    class Meta:
        model = Organizer
        fields = ['user', 'department']

class MeetingSearchForm(forms.Form):
    organizer = forms.ModelChoiceField(required=False, queryset=Organizer.objects.all())
    date_from = forms.DateField(required=False)
    date_to = forms.DateField(required=False)
    visitors = forms.ModelChoiceField(required=False, queryset=Visitor.objects.all())
    visiting_company = forms.ModelChoiceField(required=False, queryset=Company.objects.all())
    meeting_room = forms.ModelChoiceField(required=False, queryset=MeetingRoom.objects.all())


class LoginForm(forms.Form):
    username = forms.CharField(max_length=64)
    password = forms.CharField(max_length=64, widget=forms.PasswordInput)