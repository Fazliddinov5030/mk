import pytest
from rest_framework.test import APIClient
from accounts.models import User
from courses.models import Course, Category

pytestmark = pytest.mark.django_db

@pytest.fixture
def api_client():
    return APIClient()

@pytest.fixture
def instructor_user():
    return User.objects.create_user(username='instructor', password='pw', role=User.ROLE_INSTRUCTOR)

@pytest.fixture
def student_user():
    return User.objects.create_user(username='student', password='pw', role=User.ROLE_STUDENT)

class TestCourseModel:
    def test_create_course(self, instructor_user):
        category = Category.objects.create(name='Technology')
        course = Course.objects.create(
            instructor=instructor_user,
            category=category,
            title='Pytest 101',
            price='9.99',
            status=Course.Status.PUBLISHED
        )
        assert course.title == 'Pytest 101'
        assert course.instructor == instructor_user
        assert str(course) == 'Pytest 101'

class TestCourseAPI:
    def test_list_courses(self, api_client, instructor_user):
        Course.objects.create(instructor=instructor_user, title='API Course', price='19.99', status=Course.Status.PUBLISHED)
        response = api_client.get('/api/courses/')
        assert response.status_code == 200
        # Automatically handles both unpaginated (list) and paginated (dict with 'results') API responses
        assert len(response.data['results'] if 'results' in response.data else response.data) >= 1

    def test_create_course_instructor_only(self, api_client, student_user, instructor_user):
        # Ensure students receive HTTP 403 Forbidden
        api_client.force_authenticate(user=student_user)
        response = api_client.post('/api/courses/', {'title': 'Hacked Course', 'description': 'desc', 'price': '10.00'})
        assert response.status_code == 403

        # Ensure instructors successfully create courses
        api_client.force_authenticate(user=instructor_user)
        response = api_client.post('/api/courses/', {'title': 'Valid Course', 'description': 'desc', 'price': '10.00'})
        assert response.status_code == 201
