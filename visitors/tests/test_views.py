import pytest
from django.contrib.auth.models import User

from visitors.models import Company, Visitor, Comment
from meetings.models import Organizer

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