"""visits_manager URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from meetings import views as m_views
from visitors import views as v_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('mainview/', m_views.MainView.as_view(), name='main_view'),
    path('meetings_list/', m_views.MeetingsListView.as_view(), name='meetings_list'),
    path('add_meeting/', m_views.MeetingAddView.as_view(), name='add_meeting'),
    path('delete_meeting/<int:pk>/', m_views.MeetingDeleteView.as_view(), name='delete_meeting'),
    path('add_visitor/', v_views.VisitorAddView.as_view(), name='add_visitor'),
    path('visitors_list/', v_views.VisitorsListView.as_view(), name='visitors_list'),
    path('add_organizer/',  m_views.OrganizerAddView.as_view(), name='add_organizer'),
    path('add_company/', v_views.CompanyAddView.as_view(), name='add_company'),
    path('add_comment/', v_views.CommentAddView.as_view(), name='add_comment'),
    path('search_meeting/', m_views.MeetingSearchList.as_view(), name='search_meeting'),
    path('visitor_details/<int:pk>/',v_views.VisitorDetailView.as_view(), name='visitor_details' ),
]
