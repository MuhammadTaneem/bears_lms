from django.test import TestCase, Client
from rest_framework import status
from .models import Course


class CourseViewTest(TestCase):
    def setUp(self):
        self.client = Client()
        Course.objects.create(title="Python Basics", instructor="muhammad taneem", duration=10, price=19.99)

    def test_get_all_courses(self):
        response = self.client.get('/api/courses/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)

    def test_get_filtered_courses(self):
        response = self.client.get('/api/courses/?instructor=muhammad+taneem')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)

        response = self.client.get('/api/courses/?min_duration=5&max_price=25')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)

    def test_create_course(self):
        data = {
            "title": "Django Tutorial",
            "description": "Learn Django web development",
            "instructor": "Jane Smith",
            "duration": 20,
            "price": 29.99
        }
        response = self.client.post('/api/courses/', data=data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Course.objects.count(), 2)

    def test_create_course_invalid_data(self):
        data = {
            "title": "",
            "instructor": "",
            "duration": -5,
            "price": 0
        }
        response = self.client.post('/api/courses/', data=data)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(Course.objects.count(), 1)

    def test_get_course_by_id(self):
        course = Course.objects.create(title="Sample Course", instructor="Test Instructor", duration=1, price=10.00)
        response = self.client.get(f'/api/courses/{course.id}/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['title'], course.title)

    def test_get_course_by_id_not_found(self):
        response = self.client.get('/api/courses/100/')
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)


