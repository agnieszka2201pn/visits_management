import datetime

from django import views
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.mixins import PermissionRequiredMixin
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import View
from django.views.generic.list import ListView
from django.views.generic.edit import FormView, DeleteView, UpdateView

from rest_framework import generics

from search_views.search import SearchListView
from search_views.filters import BaseFilter

from meetings.forms import OrganizerAddForm, MeetingAddForm
from meetings.models import Meeting
from meetings.forms import MeetingSearchForm, LoginForm
from meetings.serializers import MeetingSerializer


class MainView(View):
    def get(self, request):
        return render(request, 'meetings/mainview.html')


class MeetingsListView(ListView):
    model = Meeting
    template_name = 'meetings/meetings_list.html'
    context_object_name = 'meetings'


class MeetingAddView(PermissionRequiredMixin, FormView):
    permission_required = 'meetings.add_meeting'
    permission_denied_message = "you do not have permission to add meetings"
    template_name = 'meetings/add_meeting.html'
    form_class = MeetingAddForm
    success_url = reverse_lazy('meetings_list')

    def form_valid(self,form):
        cd = form.cleaned_data
        date = cd['date']
        if date < datetime.date.today():
            return HttpResponse('you cannot organize a meeting in the past')
        else:
            meetings = list(Meeting.objects.filter(date=date))
            rooms = []
            if meetings:
                for meeting in meetings:
                    room = meeting.meeting_room
                    rooms.append(room)
            if cd['meeting_room'] in rooms:
                return HttpResponse('this room is already booked')
            else:
                form.save()
        return super().form_valid(form)


class MeetingDeleteView(PermissionRequiredMixin, DeleteView):
    permission_required = 'meetings.delete_meeting'
    permission_denied_message = "you do not have permission to delete meetings"
    model = Meeting
    success_url = reverse_lazy('meetings_list')


class MeetingUpdate(PermissionRequiredMixin, UpdateView):
    permission_required = 'meetings.change_meeting'
    permission_denied_message = "you do not have permission to update meetings"
    model = Meeting
    fields = ['organizer', 'date', 'visitors', 'meeting_room', 'note']
    template_name_suffix = '_update_form'
    success_url = reverse_lazy('meetings_list')

    def get_initial(self):
        initial_data = super().get_initial()
        initial_data['meeting.pk'] = self.kwargs['pk']
        return initial_data

    def form_valid(self,form):
        cd = form.cleaned_data
        date = cd['date']
        if date < datetime.date.today():
            return HttpResponse('you cannot organize a meeting in the past')
        else:
            pk = self.get_initial()['meeting.pk']
            meeting = Meeting.objects.get(pk=pk)
            if cd['meeting_room'] == meeting.meeting_room:
                form.save()
            else:
                meetings = Meeting.objects.filter(date=date)
                rooms = []
                if meetings:
                    for meeting in meetings:
                        room = meeting.meeting_room
                        rooms.append(room)
                if cd['meeting_room'] in rooms:
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
    success_url = reverse_lazy('main_view')

    def form_valid(self,form):
        form.save()
        return super().form_valid(form)


class MeetingListApi(generics.ListCreateAPIView):
    queryset = Meeting.objects.all()
    serializer_class = MeetingSerializer


class MeetingView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Meeting.objects.all()
    serializer_class = MeetingSerializer


class LoginView(views.View):
    def get(self,request):
        form = LoginForm()
        return render(request, 'meetings/login.html', {'form':form})

    def post(self, request):
        form = LoginForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            username = cd['username']
            password = cd['password']
            user1 = authenticate(username=username, password=password)
            if user1:
                login(request,user1)
                return HttpResponseRedirect('/mainview/')
            else:
                return HttpResponse('user does not exist')


class LogoutView(views.View):
    def get(self, request):
        return render(request, 'meetings/logout.html')

    def post(self, request):
        logout(request)
        return HttpResponseRedirect('/login/')
