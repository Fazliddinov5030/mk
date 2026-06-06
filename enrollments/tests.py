import pytest
from rest_framework.test import APIClient
from accounts.models import User
from courses.models import Course
from enrollments.models import Enrollment

pytestmark = pytest.mark.django_db

@pytest.fixture
def api_client():
    return APIClient()

@pytest.fixture
def student_user():
    return User.objects.create_user(username='student1', password='pw', role=User.ROLE_STUDENT)

@pytest.fixture
def course():
    instructor = User.objects.create_user(username='inst', password='pw', role=User.ROLE_INSTRUCTOR)
    return Course.objects.create(
        title='Test Course',
        instructor=instructor,
        price='50.00',
        status=Course.Status.PUBLISHED
    )

class TestEnrollmentModel:
    def test_create_enrollment(self, student_user, course):
        enrollment = Enrollment.objects.create(user=student_user, course=course)
        assert enrollment.user == student_user
        assert enrollment.course == course
        assert enrollment.is_completed is False

class TestEnrollmentAPI:
    def test_enrollment_requires_student_role(self, api_client, course):
        instructor = User.objects.create_user(username='inst2', password='pw', role=User.ROLE_INSTRUCTOR)
        api_client.force_authenticate(user=instructor)
        response = api_client.post('/api/enrollments/enrollments/enroll/', {'course_id': course.id})
        assert response.status_code == 403
