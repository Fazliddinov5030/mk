import pytest
from accounts.models import User

pytestmark = pytest.mark.django_db

class TestUserModel:
    def test_create_user_student(self):
        user = User.objects.create_user(username='student1', email='student@test.com', password='pw')
        assert user.username == 'student1'
        assert user.role == User.ROLE_STUDENT

    def test_create_user_instructor(self):
        user = User.objects.create_user(username='instructor1', password='pw', role=User.ROLE_INSTRUCTOR)
        assert user.role == User.ROLE_INSTRUCTOR

    def test_user_str_representation(self):
        user = User.objects.create_user(username='johndoe', password='pw')
        assert str(user) == 'johndoe'
