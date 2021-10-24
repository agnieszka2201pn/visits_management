from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import View
from django.views.generic.list import ListView
from django.views.generic.edit import FormView
from django.shortcuts import render

from visitors.forms import VisitorAddForm
from visitors.models import Visitor


class VisitorAddView(FormView):
    template_name = 'visitors/add_visitor.html'
    form_class = VisitorAddForm
    success_url = reverse_lazy('meetings_list')

    def form_valid(self,form):
        form.save()
        return super().form_valid(form)


class VisitorsListView(ListView):
    model = Visitor
    template_name = 'visitors/visitors_list.html'
    context_object_name = 'visitors'