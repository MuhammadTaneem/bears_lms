## Bears LMS  Project

This project is a Dockerized version of Bears LMS, a Learning Management System.

## installation Guide

### Prerequisites

Before you begin, ensure you have the following prerequisites installed on your system:

- Docker
- Docker Compose

### Steps to Setup

1. **Clone the Repository:**

    ```bash
    git clone https://github.com/MuhammadTaneem/bears_lms.git
    ```

2. **Navigate to Project Directory:**

    ```bash
    cd bears_lms
    ```

3. **Build and Run Docker Containers:**

    ```bash
    docker-compose up -d --build
    ```


4. **Access the Application:**

    The Bears LMS application will be accessible at [http://localhost:8000/](http://localhost:8000/).


## API guide
### 1. Get All Courses
- **URL:** `api/courses/`
- **Method:** GET
- **Description:** Retrieves a list of all courses.Also allows filtering by instructor, price, and duration.
- **Parameters:** 
  - `instructor`: Filters courses by instructor name.
  - `min_price`: Filters courses with a price greater than or equal value.
  - `max_price`: Filters courses with a price less than or equal value.
  - `min_duration`: Filters courses with a duration greater than or equal value.
  - `max_duration`: Filters courses with a duration less than or equal value.
- **Example Request:**
```bash
GET http://localhost:8000/api/courses/?instructor=nahid&min_price=50&max_duration=60
```

- **Example Response:**
```json
[
    {
        "id": 1,
        "title": "Course Title",
        "description": "Course Description",
        "instructor": "John",
        "duration": 60,
        "price": 100.0
    },
    {
        "id": 2,
        "title": "Another Course",
        "description": "",
        "instructor": "John",
        "duration": 45,
        "price": 75.0
    }
]
```
### 2. Get Course by ID
- **URL:** `api/courses/<course_id>/`
- **Method:** GET
- **Description:**  Retrieves details of a specific course by its ID.


- **Example Request:**
```bash
 GET http://localhost:8000/api/courses/1/
 ```
- **Example Response:**
```bash
{
    "id": 1,
    "title": "Course Title",
    "description": "Course Description",
    "instructor": "John",
    "duration": 60,
    "price": 100.0
}
```


### 3. Create a New Course
- **URL:** `api/courses/`
- **Method:** POST
- **Description:**  Creates a new course with the provided details.
- **Example Request:**

```bash
POST http://localhost:8000/api/courses/
Content-Type: application/json

{
    "title": "New Course",
    "description": "Description of the new course",
    "instructor": "hasan",
    "duration": 45,
    "price": 80.0
}
```

- **Example Response**
```bash
{
    "id": 3,
    "title": "New Course",
    "description": "Description of the new course",
    "instructor": "Jane",
    "duration": 45,
    "price": 80.0
}

```

### 4 .Enroll Student in a Course
- **URL:** `api/enrollments/`
- **Method:** POST
- **Description:**  Enrolls a student in a specific course..
- **Example Request:**

```bash
POST http://localhost:8000/api/enrollments/
Content-Type: application/json

{
    "student_name": "rafik",
    "course_id": 1
}

```

- **Example Response**
```bash
{
    "id": 1,
    "student_name": "re",
    "enrollment_date": "2024-04-06",
    "course": 1
}
```


### Running Tests

To see the test code results, run the following command:

```bash
docker-compose exec app python manage.py test
```
