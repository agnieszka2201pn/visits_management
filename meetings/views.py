import datetime

from django.http import HttpResponse
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import DetailView
from django.views.generic.list import ListView
from django.views.generic.edit import FormView, DeleteView, UpdateView

from search_views.search import SearchListView
from search_views.filters import BaseFilter

from meetings.forms import OrganizerAddForm, MeetingAddForm
from meetings.models import Meeting
from meetings.forms import MeetingSearchForm


class MainView(View):
    def get(self, request):
        return render(request, 'meetings/mainview.html')


class MeetingsListView(ListView):
    model = Meeting
    paginate_by = 10
    template_name = 'meetings/meetings_list.html'
    context_object_name = 'meetings'


class MeetingAddView(FormView):
    template_name = 'meetings/add_meeting.html'
    form_class = MeetingAddForm
    success_url = reverse_lazy('meetings_list')

    def form_valid(self,form):
        cd = form.cleaned_data
        date = cd['date']
        if date < datetime.date.today():
            return HttpResponse('you cannot organize a meeting in the past')
        else:
            meeting = Meeting.objects.filter(date=date)
            if meeting:
                meeting = Meeting.objects.get(date=date)
                room = meeting.meeting_room
                if room == cd['meeting_room']:
                    return HttpResponse('this room is already booked')
            else:
                form.save()
        return super().form_valid(form)


class MeetingDeleteView(DeleteView):
    model = Meeting
    success_url = reverse_lazy('meetings_list')


class MeetingUpdate(UpdateView):
    model = Meeting
    fields = ['organizer', 'date', 'visitors', 'meeting_room', 'note']
    template_name_suffix = '_update_form'
    success_url = reverse_lazy('meetings_list')

    def form_valid(self,form):
        cd = form.cleaned_data
        date = cd['date']
        if date < datetime.date.today():
            return HttpResponse('you cannot organize a meeting in the past')
        else:
            meeting = Meeting.objects.filter(date=date)
            if meeting:
                meeting = Meeting.objects.get(date=date)
                room = meeting.meeting_room
                if room == cd['meeting_room']:
                    return HttpResponse('this room is already booked')
            else:
                form.save()
        return super().form_valid(form)


class MeetingFilter(BaseFilter):
    search_fields = {
        'organizer' : ['organizer__pk'],
        'date_from' : {'operator':'__gte', 'fields':['date']},
        'date_to' : {'operator':'__lte', 'fields':['date']},
        'visitors' : ['visitors__pk'],
        'visiting_company': ['visitors__company__pk'],
        'meeting_room' : ['meeting_room__pk'],
    }


class MeetingSearchList(SearchListView):
    model = Meeting
    template_name = 'meetings/meetings_search.html'
    form_class = MeetingSearchForm
    filter_class = MeetingFilter



class OrganizerAddView(FormView):
    template_name = 'meetings/add_organizer.html'
    form_class = OrganizerAddForm
    success_url = reverse_lazy('meetings_list')

    def form_valid(self,form):
        form.save()
        return super().form_valid(form)
