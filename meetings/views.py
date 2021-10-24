from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import View
from django.views.generic.list import ListView
from django.views.generic.edit import FormView

from meetings.forms import AddMeetingForm
from meetings.models import Meeting


class MainView(View):
    def get(self, request):
        return render(request, 'meetings/mainview.html')


class MeetingsListView(ListView):
    model = Meeting
    template_name = 'meetings/meetings_list.html'
    context_object_name = 'meeting'


class MeetingAddView(FormView):
    template_name = 'meetings/add_meeting.html'
    form_class = AddMeetingForm
    success_url = reverse_lazy('meetings_list')

    def form_valid(self,form):
        form.save()
        return super().form_valid(form)
