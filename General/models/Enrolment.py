from django.db import models
from django.contrib.auth.models import User

from General.models.Group import Group
from General.models.Student import Student

class Enrolment(models.Model):
    group = models.ForeignKey(Group, related_name="enrolments", on_delete=models.PROTECT)
    student = models.ForeignKey(Student, related_name="enrolments", on_delete=models.PROTECT)
    enrolmentCost = models.FloatField()

