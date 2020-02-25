import json

from django.test import TestCase

from django.contrib.auth.models import User
from django.urls import reverse
from rest_framework.authtoken.models import Token
from rest_framework.test import APITestCase
from rest_framework import status

from courses.models import Course, Comment, Material, Teacher, Video
from courses.serializers import (
    CourseSerializer, CourseDetailSerializer, CommentSerializer, 
    TeacherSerializer, MaterialSerializer, VideoSerializer
    )

 
class CoursesTestCase(APITestCase):
    url = reverse('courses-list')

    def setUp(self):
        self.username = "John Doe"
        self.password = "this_is_a_test"
        self.user = User.objects.create_user(
            self.username, self.password
        )
        self.token = Token.objects.create(user=self.user)
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + self.token.key)

    def test_create_new_course(self):
        print('create a new course with id 1...')

        data = {
                "name": "Curso de Selenium",
                "description": "Curso de Selenium",
                "teachers": 
                [
                    {
                        "name": "Hector Vega",
                        "description": "QA engineer",
                        "current_job": "QA engineer"
                    }
                ]
            }
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + self.token.key)
        response = self.client.post(self.url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
    
    def test_get_courses(self):
        print('get list of courses...')
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + self.token.key)
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)



        
