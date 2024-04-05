from django.test import TestCase
from rest_framework import status
from rest_framework.test import APIClient

from Courses.models import Course
from .models import Enrollment
from .serializers import EnrollmentSerializer


class EnrollmentTest(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.test_course = Course.objects.create(title="Python Basics", instructor="muhammad taneem", duration=10,
                                                 price=19.99)

    def test_enroll_student_success(self):
        data = {
            "student_name": "Tafhimul ihsan",
            "course_id": self.test_course.id
        }
        response = self.client.post("/api/enrollments/", data=data, format="json")
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        serializer = EnrollmentSerializer(Enrollment.objects.get(pk=response.data["id"]))
        self.assertEqual(serializer.data, response.data)

    def test_enroll_student_missing_field(self):
        data = {"course_id": self.test_course.id}
        response = self.client.post("/api/enrollments/", data=data, format="json")
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_enroll_student_non_existent_course(self):
        data = {"student_name": "nahid", "course_id": -1}
        response = self.client.post("/api/enrollments/", data=data, format="json")
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertIn("Course id must be a positive integer.", response.content.decode())
