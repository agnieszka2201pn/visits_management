from django.forms import ModelForm

from meetings.models import Meeting, Organizer


class AddMeetingForm(ModelForm):
    class Meta:
        model = Meeting
        fields = ['organizer', 'date', 'visitors', 'meeting_room', 'note']


class OrganizerAddForm(ModelForm):
    class Meta:
        model = Organizer
        fields = ['user', 'department']