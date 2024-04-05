from django.db import models
from Courses.models import Course


class Enrollment(models.Model):
    student_name = models.CharField(max_length=255)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    enrollment_date = models.DateField(auto_now_add=True)
