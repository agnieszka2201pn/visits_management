from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import View
from django.views.generic.list import ListView
from django.views.generic.edit import FormView
from django.shortcuts import render

from visitors.forms import VisitorAddForm, CompanyAddForm, CommentAddForm
from visitors.models import Visitor


class VisitorAddView(FormView):
    template_name = 'visitors/add_visitor.html'
    form_class = VisitorAddForm
    success_url = reverse_lazy('main_view')

    def form_valid(self,form):
        form.save()
        return super().form_valid(form)


class VisitorsListView(ListView):
    model = Visitor
    template_name = 'visitors/visitors_list.html'
    context_object_name = 'visitors'


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
    success_url = reverse_lazy('main_view')

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)