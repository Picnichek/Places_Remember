import pytest
from django.contrib.auth import get_user_model
from places.models import Memory

User = get_user_model()


@pytest.mark.django_db
def test_memory_creation():
    user = User.objects.create_user(
        username='test_user', email='test@example.com', password='testpassword')
    memory = Memory.objects.create(
        user=user,
        title='Test Memory',
        location='Test Location',
        comment='Test Comment',
        latitude=0.0,
        longitude=0.0
    )
    assert memory.user == user
    assert memory.title == 'Test Memory'
    assert memory.location == 'Test Location'
    assert memory.comment == 'Test Comment'
    assert memory.latitude == 0.0
    assert memory.longitude == 0.0
