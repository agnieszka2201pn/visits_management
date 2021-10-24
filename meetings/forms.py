from django.forms import ModelForm

from meetings.models import Meeting


class AddMeetingForm(ModelForm):
    class Meta:
        model = Meeting
        fields = ['organizer', 'date', 'visitors', 'meeting_room', 'note']