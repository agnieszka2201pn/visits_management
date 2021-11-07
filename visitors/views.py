from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import DetailView
from django.views.generic.list import ListView
from django.views.generic.edit import FormView, UpdateView
from django.shortcuts import render

from search_views.search import SearchListView
from search_views.filters import BaseFilter

from rest_framework import generics

from visitors.forms import VisitorAddForm, CompanyAddForm, CommentAddForm, VisitorSearchForm
from visitors.models import Visitor
from visitors.serializers import VisitorSerializer


class VisitorAddView(FormView):
    template_name = 'visitors/add_visitor.html'
    form_class = VisitorAddForm
    success_url = reverse_lazy('visitors_list')

    def form_valid(self,form):
        form.save()
        return super().form_valid(form)


class VisitorsListView(ListView):
    queryset = Visitor.objects.all().order_by('surname')
    template_name = 'visitors/visitors_list.html'
    context_object_name = 'visitors'


class UpdateVisitor(UpdateView):
    model = Visitor
    fields = ['first_name', 'surname', 'contact_details', 'company', 'last_training_date']
    template_name_suffix = '_update_form'
    success_url = reverse_lazy('visitors_list')


class CompanyAddView(FormView):
    template_name = 'visitors/add_company.html'
    form_class = CompanyAddForm
    success_url = reverse_lazy('main_view')

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)


class CommentAddView(FormView):
    template_name = 'visitors/add_comment.html'
    form_class = CommentAddForm
    success_url = reverse_lazy('visitors_list')

    def get_initial(self):
        initial_data = super().get_initial()
        initial_data['visitor'] = self.kwargs['pk']
        return initial_data


    def form_valid(self, form):
        form.save()
        return super().form_valid(form)


class VisitorFilter(BaseFilter):
    search_fields = {
        'name' : ['pk'],
        'company': ['company__pk'],
        'last_training_date' : {'operator':'__gte', 'fields':['last_training_date']},
    }


class VisitorSearchList(SearchListView):
    model = Visitor
    template_name = 'visitors/visitors_search.html'
    form_class = VisitorSearchForm
    filter_class = VisitorFilter


class VisitorView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Visitor.objects.all()
    serializer_class = VisitorSerializer


class VisitorListApi(generics.ListCreateAPIView):
    queryset = Visitor.objects.all()
    serializer_class = VisitorSerializer