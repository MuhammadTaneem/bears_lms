from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Course
from .serializers import CourseSerializer


@api_view(['GET', 'POST'])
def course_view(request):
    # this get method view is for getting all course
    # also return filtered course data
    if request.method == 'GET':
        courses = Course.objects.all()
        if 'instructor' in request.GET:
            instructor = request.GET['instructor']
            courses = courses.filter(instructor__exact=instructor)
        if 'min_price' in request.GET:
            min_price = float(request.GET['min_price'])
            courses = courses.filter(price__gte=min_price)
        if 'max_price' in request.GET:
            max_price = float(request.GET['max_price'])
            courses = courses.filter(price__lte=max_price)
        if 'min_duration' in request.GET:
            min_duration = int(request.GET['min_duration'])
            courses = courses.filter(duration__gte=min_duration)
        if 'max_duration' in request.GET:
            max_duration = int(request.GET['max_duration'])
            courses = courses.filter(duration__lte=max_duration)
        serializer = CourseSerializer(courses, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    # this is course create view
    elif request.method == 'POST':
        data = request.data
        try:
            title = data['title']

            if not title or not title.strip():
                raise ValueError("Title is required and cannot be empty.")

            description = data['description'] if data['description'] else ''

            instructor = data['instructor']
            if not instructor or not instructor.strip():
                raise ValueError("Instructor name is required and cannot be empty.")

            try:
                duration = int(data['duration'])
                if duration <= 0:
                    raise ValueError("Duration must be a positive integer.")

            except (ValueError, TypeError):
                raise ValueError("Duration must be a positive integer.")

            try:
                price = float(data['price'])
                if price <= 0:
                    raise ValueError("Price must be a positive number.")

            except (ValueError, TypeError) as e:
                raise ValueError(f"Invalid price: {e}") from e

        except KeyError as e:
            return Response(f"Missing required field: {e}", status=status.HTTP_400_BAD_REQUEST)
        except ValueError as e:
            return Response(f"Validation error: {e}", status=status.HTTP_400_BAD_REQUEST)

        try:
            course = Course.objects.create(
                title=title,
                description=description,
                instructor=instructor,
                duration=duration,
                price=price
            )
        except Exception as e:
            print(f"Error creating course: {e}")
            return Response("Failed to create course due to an error.", status=status.HTTP_500_INTERNAL_SERVER_ERROR)

        if course:
            serializer = CourseSerializer(course)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response("Failed to create course", status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    else:
        return Response(f"Invalid request method. {request.method} is not allowed.",
                        status=status.HTTP_405_METHOD_NOT_ALLOWED)


# get course by id
@api_view(['GET'])
def get_course_by_id(request, course_id):
    try:
        course = Course.objects.get(id=course_id)
        serializer = CourseSerializer(course)
        return Response(serializer.data, status=status.HTTP_200_OK)
    except Course.DoesNotExist:
        return Response("Course dose not found.", status=status.HTTP_404_NOT_FOUND)


