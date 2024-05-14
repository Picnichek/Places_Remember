import pytest
from django.contrib.auth import get_user_model
from django.urls import reverse
from django.test import Client
from places.models import Memory

User = get_user_model()


@pytest.fixture
def logged_in_client():
    user = User.objects.create_user(
        username='admin', email='test@example.com', password='testpassword')
    client = Client()
    client.login(username='admin', password='testpassword')
    return client, user


@pytest.fixture
def logged_in_another_client():
    user = User.objects.create_user(
        username='test_username', email='test@example.com', password='testpassword')
    client = Client()
    client.login(
        username='test_username', password='testpassword')
    return client, user


@pytest.fixture
def memories():
    memories = [
        {
            'title': 'Test Memory1',
            'location': 'Test Location1',
            'comment': 'Test Comment1',
            'latitude': 0.0,
            'longitude': 0.0},
        {
            'title': 'Test Memory2',
            'location': 'Test Location2',
            'comment': 'Test Comment2',
            'latitude': 1.0,
            'longitude': 1.0},
        {
            'title': 'Test Memory3',
            'location': 'Test Location3',
            'comment': 'Test Comment3',
            'latitude': 2.0,
            'longitude': 2.0},
    ]
    return memories


@pytest.mark.django_db
def test_add_memory_view(logged_in_client, memories):
    client, user = logged_in_client
    url = reverse('places:add_memory')
    response = client.get(url)
    assert response.status_code == 200

    for memory in memories:
        response = client.post(url, memory)
        assert response.status_code == 302
    assert len(Memory.objects.filter(title__contains='Test Memory')) == 3


@pytest.mark.django_db
def test_edit_memory_view(logged_in_client, memories):
    client, user = logged_in_client
    memory = Memory.objects.create(
        user=user,
        title=memories[0]['title'],
        location=memories[0]['location'],
        comment=memories[0]['comment'],
        latitude=memories[0]['latitude'],
        longitude=memories[0]['longitude']
    )
    url = reverse('places:edit_memory', kwargs={'memory_id': memory.pk})
    response = client.get(url)
    assert response.status_code == 200

    response = client.post(url, {
        'title': 'Updated Memory',
        'location': 'Updated Location',
        'comment': 'Updated Comment',
        'latitude': 1.0,
        'longitude': 1.0
    })
    assert response.status_code == 302
    memory.refresh_from_db()
    assert memory.title == 'Updated Memory'
    assert memory.location == 'Updated Location'
    assert memory.comment == 'Updated Comment'
    assert memory.latitude == 1.0
    assert memory.longitude == 1.0


@pytest.mark.django_db
def test_delete_memory_view(logged_in_client, memories):
    client, user = logged_in_client
    memory = Memory.objects.create(
        user=user,
        title=memories[0]['title'],
        location=memories[0]['location'],
        comment=memories[0]['comment'],
        latitude=memories[0]['latitude'],
        longitude=memories[0]['longitude']
    )
    url = reverse('places:delete_memory', kwargs={'memory_id': memory.pk})
    response = client.get(url)
    assert response.status_code == 200

    response = client.post(url)
    assert response.status_code == 302
    assert not Memory.objects.filter(pk=memory.pk).exists()


@pytest.mark.django_db
def test_home_view(logged_in_client, logged_in_another_client, memories):
    client, user = logged_in_client
    another_client, another_user = logged_in_another_client
    for memory in memories:
        Memory.objects.create(
            user=user,
            title=memory['title'],
            location=memory['location'],
            comment=memory['comment'],
            latitude=memory['latitude'],
            longitude=memory['longitude']
        )

    response = client.get(reverse('places:home'))
    another_response = another_client.get(reverse('places:home'))
    assert response.status_code == 200
    assert another_response.status_code == 200

    assert 'Test Memory1' in response.content.decode('utf-8')
    assert 'Test Memory2' in response.content.decode('utf-8')
    assert 'Test Memory3' in response.content.decode('utf-8')

    assert 'Test Memory1' not in another_response.content.decode('utf-8')
    assert 'Test Memory2' not in another_response.content.decode('utf-8')
    assert 'Test Memory3' not in another_response.content.decode('utf-8')
