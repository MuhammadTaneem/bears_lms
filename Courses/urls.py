from django.urls import path
from .views import course_view, get_course_by_id

urlpatterns = [
    path('', course_view, name='courses'),  # get all courses , filtering, creating
    path('<int:course_id>/', get_course_by_id, name='get_course_by_id'),  # specific course by ID
]
