from django.db import models
from django.contrib.auth.models import User

from General.models.Lesson import Lesson
from General.models.Student import Student

class Attendance(models.Model):
    student = models.ForeignKey(Student, related_name="attendedLessons" ,on_delete=models.CASCADE)
    lesson = models.ForeignKey(Lesson, related_name="attendances", on_delete=models.CASCADE)
    trial = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.student} - {self.lesson} (Attendance)"

