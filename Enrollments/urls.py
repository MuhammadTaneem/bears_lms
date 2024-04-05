from django.urls import path
from .views import enroll_student

urlpatterns = [
    path('', enroll_student, name='enrollment'),  # get all courses , filtering, creating
]
