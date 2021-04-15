from django.test import TestCase
from . import models


# Create your tests here.
user_student = models.UserStudent.objects.get(name="沈文心")
print(user_student)