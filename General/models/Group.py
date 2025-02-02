from django.db import models
from django.contrib.auth.models import User

from General.models.Tutor import Tutor

class Group(models.Model):
    YEAR_CHOICES = [
        ('K', 'K'),
        ('1', '1'),
        ('2', '2'),
        ('3', '3'),
        ('4', '4'),
        ('5', '5'),
        ('6', '6'),
        ('7', '7'),
        ('8', '8'),
        ('9', '9'),
        ('10', '10'),
        ('11', '11'),
        ('12', '12'),
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
        return f"{self.get_year_display()} - {self.get_subject_display()} - {self.get_lesson_type_display()}"

    @property
    def estimatedProfit(self):
        revenue = 0.00
        enrolments = self.enrolments.all()
        for enrolment in enrolments:
            revenue += enrolment.enrolmentCost

        return revenue - self.cost

    def enrolStudent():
        ...
    
