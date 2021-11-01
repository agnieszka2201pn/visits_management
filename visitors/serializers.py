from rest_framework import serializers
from visitors.models import Visitor

class VisitorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Visitor
        fields = ['id', 'first_name', 'surname', 'contact_details', 'company', 'last_training_date']