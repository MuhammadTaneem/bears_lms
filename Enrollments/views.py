from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from Courses.models import Course
from .models import Enrollment
from .serializers import EnrollmentSerializer


@api_view(['POST'])
def enroll_student(request):
    data = request.data
    try:
        student_name = data['student_name']
        if not student_name or not student_name.strip():
            raise ValueError("Title is required and cannot be empty.")

        try:
            course_id = int(data['course_id'])
            if course_id <= 0:
                raise ValueError("course id must be a positive integer.")

        except (ValueError, TypeError):
            raise ValueError("Course id must be a positive integer.")



    except KeyError as e:
        return Response(f"Missing required field: {e}", status=status.HTTP_400_BAD_REQUEST)
    except ValueError as e:
        return Response(f"Validation error: {e}", status=status.HTTP_400_BAD_REQUEST)

    course = validate_enrollment(course_id)
    if not course:
        return Response('Course not found', status=status.HTTP_404_NOT_FOUND)

    try:
        enrollment = Enrollment.objects.create(
            student_name=student_name,
            course=course
        )
    except Exception as e:
        print(f"Error creating course: {e}")
        return Response("Failed to create enrollment due to an error.", status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    if enrollment:
        serializer = EnrollmentSerializer(enrollment)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    else:
        return Response("Failed to create enrollment", status=status.HTTP_500_INTERNAL_SERVER_ERROR)


def validate_enrollment(course_id):
    try:
        return Course.objects.get(pk=course_id)
    except Course.DoesNotExist:
        return False
