from django.http import HttpResponse
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import View
from django.views.generic.list import ListView
from django.views.generic.edit import FormView, DeleteView

from meetings.forms import AddMeetingForm, OrganizerAddForm
from meetings.models import Meeting


class MainView(View):
    def get(self, request):
        return render(request, 'meetings/mainview.html')


class MeetingsListView(ListView):
    model = Meeting
    template_name = 'meetings/meetings_list.html'
    context_object_name = 'meetings'


class MeetingAddView(FormView):
    template_name = 'meetings/add_meeting.html'
    form_class = AddMeetingForm
    success_url = reverse_lazy('meetings_list')

    def form_valid(self,form):
        cd = form.cleaned_data
        date = cd['date']
        meeting = Meeting.objects.get(date=date)
        if meeting:
            room = meeting.meeting_room
            if room == cd['meeting_room']:
                return HttpResponse('this room is already booked')
        else:
            form.save()
        return super().form_valid(form)


class MeetingDeleteView(DeleteView):
    model = Meeting
    success_url = reverse_lazy('meetings_list')


class OrganizerAddView(FormView):
    template_name = 'meetings/add_organizer.html'
    form_class = OrganizerAddForm
    success_url = reverse_lazy('meetings_list')

    def form_valid(self,form):
        form.save()
        return super().form_valid(form)

