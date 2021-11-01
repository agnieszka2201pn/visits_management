from rest_framework import serializers
from meetings.models import Meeting

class MeetingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Meeting
        fields = ['id', 'organizer', 'date', 'visitors', 'meeting_room', 'note']