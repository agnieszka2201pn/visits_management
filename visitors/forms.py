from django.forms import ModelForm

from visitors.models import Visitor


class VisitorAddForm(ModelForm):
    class Meta:
        model = Visitor
        fields = ['first_name', 'surname', 'contact_details', 'company', 'last_training_date']