from datetime import datetime

import pytest
from django.contrib.auth.models import User

from visitors.models import Company, Visitor, Comment
from meetings.models import Organizer, Meeting, MeetingRoom

@pytest.mark.django_db
def test_company_add_view(client):
    url = '/add_company/'
    name = 'company1'
    company_type = 1
    response = client.post(url, {'name':name, 'company_type':company_type})
    assert response.status_code == 302
    assert Company.objects.count() == 1


@pytest.mark.django_db
def test_visitor_add_view(client):
    url = '/add_visitor/'
    company = Company.objects.create(name='company_name', company_type=1)
    response = client.post(url, {'first_name':'visitor',
                                 'surname':'visitor_surname',
                                 'contact_details':'visitor@gmail.com',
                                 'company':company.pk})
    assert response.status_code == 302
    assert Visitor.objects.count() == 1


@pytest.mark.django_db
def test_comment_add_view(client):
    company = Company.objects.create(name='company_name', company_type=1)
    user = User.objects.create(username="user1")
    author = Organizer.objects.create(user=user, department=1)
    visitor = Visitor.objects.create(first_name='aaa',
                                     surname='bbb',
                                     contact_details='blablabla',
                                     company = company)
    url = f'/add_comment/{visitor.pk}/'
    response = client.post(url, { 'content' : 'fake_comment','author': author.pk, 'visitor': visitor.pk})
    assert response.status_code == 302
    assert Comment.objects.count() == 1


@pytest.mark.django_db
def test_visitors_list_view(visitors, client):
    url = '/visitors_list/'
    response = client.get(url)
    assert response.status_code == 200
    list_view = list(response.context['visitors'].values_list('pk', flat=True))
    list_db = list(Visitor.objects.all().values_list('pk', flat=True))
    assert list_view == list_db


@pytest.mark.django_db
def test_visitor_update_view(visitors, client):
    visitor = visitors[0]
    url = f'/update_visitor/{visitor.pk}/'
    response_get = client.get(url)
    visitor_data = response_get.context['form'].initial
    visitor_data['first_name'] = 'new name'
    visitor_data['last_training_date'] = datetime.today().strftime('%Y-%m-%d')
    response = client.post(url, visitor_data)
    changed_visitor = Visitor.objects.get(pk=visitor.pk)
    assert changed_visitor.first_name == 'new name'
    assert response.status_code == 302


@pytest.mark.django_db
def test_visitor_search_view(visitors, client):
    visitor1 = visitors[0]
    company = visitor1.company
    url = f'/search_visitor/'
    response = client.get(url, {'company': company.pk})
    assert len(response.context_data['visitor_list']) == len(Visitor.objects.filter(company=company.pk))
    assert response.status_code == 200

