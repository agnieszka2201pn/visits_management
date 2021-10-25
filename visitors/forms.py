from django.forms import ModelForm

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