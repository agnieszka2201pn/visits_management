from django.forms import ModelForm
from django import forms

from visitors.models import Visitor, Company, Comment


class VisitorAddForm(ModelForm):
    class Meta:
        model = Visitor
        fields = ['first_name', 'surname', 'contact_details', 'company', 'last_training_date']


class CompanyAddForm(ModelForm):
    class Meta:
        model = Company
        fields = ['name', 'company_type']


class CommentAddForm(ModelForm):
    class Meta:
        model = Comment
        fields = ['content', 'author', 'visitor']
        widgets = {'visitor':forms.widgets.HiddenInput}

class VisitorSearchForm(forms.Form):
    name = forms.ModelChoiceField(required=False, queryset=Visitor.objects.all())
    company = forms.ModelChoiceField(required=False, queryset=Company.objects.all())
    last_training_date = forms.DateField(required=False)