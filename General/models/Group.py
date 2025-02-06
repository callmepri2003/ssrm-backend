from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse

from General.models.Tutor import Tutor
from django.utils.translation import gettext_lazy as _

class Group(models.Model):
    YEAR_CHOICES = [
        ('K', 'Kindergarten'),
        ('1', 'Year 1'),
        ('2', 'Year 2'),
        ('3', 'Year 3'),
        ('4', 'Year 4'),
        ('5', 'Year 5'),
        ('6', 'Year 6'),
        ('7', 'Year 7'),
        ('8', 'Year 8'),
        ('9', 'Year 9'),
        ('10', 'Year 10'),
        ('11', 'Year 11'),
        ('12', 'Year 12'),
        ('S', 'Selective'),
    ]

    SUBJECT_CHOICES = [
        ('jnr', 'Junior Mathematics'),
        ('adv', 'Mathematics Advanced'),
        ('gnl', 'Mathematics Standard'),
        ('ext1', 'Mathematics Extension 1'),
        ('ext2', 'Mathematics Extension 2'),
        ('oth', 'Other')
    ]

    LESSON_TYPE_CHOICES = [
        ('group', 'Group Lessons'),
        ('private', 'Private Lessons'),
    ]


    cost = models.FloatField()
    tutor = models.ForeignKey(Tutor, on_delete=models.PROTECT, related_name='groups')
    year = models.CharField(max_length=2, choices=YEAR_CHOICES)
    subject = models.CharField(max_length=4, choices=SUBJECT_CHOICES)
    lesson_type = models.CharField(max_length=10, choices=LESSON_TYPE_CHOICES)
    notes = models.TextField()

    def __str__(self):
        students = []
        for enrolment in self.enrolments.all():
            students.append(str(enrolment.student))
        return f"{self.get_year_display()} - {self.get_subject_display()} - {self.get_lesson_type_display()} - {students}"

    @property
    def estimatedProfit(self):
        revenue = 0.00
        enrolments = self.enrolments.all()
        for enrolment in enrolments:
            revenue += enrolment.enrolmentCost

        return revenue - self.cost

    def enrolStudent():
        ...

class When(models.Model):
    DAY_CHOICES = [
        ('Mon', 'Monday'),
        ('Tue', 'Tuesday'),
        ('Wed', 'Wednesday'),
        ('Thu', 'Thursday'),
        ('Fri', 'Friday'),
        ('Sat', 'Saturday'),
        ('Sun', 'Sunday'),
    ]

    TIME_CHOICES = [
        (f"{hour:02d}:{minute:02d}", f"{hour:02d}:{minute:02d}")
        for hour in range(7, 22)  # 7 AM to 9 PM
        for minute in (0, 15, 30, 45)  # 15-minute intervals
    ]

    day = models.CharField(max_length=3, choices=DAY_CHOICES)
    time = models.CharField(max_length=5, choices=TIME_CHOICES)
    length_hours = models.IntegerField()
    group = models.ForeignKey(Group, on_delete=models.CASCADE, related_name='schedules')


    class Meta:
        verbose_name = _("Schedule")
        verbose_name_plural = _("Schedules")

    def __str__(self):
        return f"{self.get_day_display()} at {self.time}"
