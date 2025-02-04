from django.db import models
from django.contrib.auth.models import User
from .Group import Group
from .Tutor import Tutor

class Lesson(models.Model):
    STATUS_CHOICES = [
        ('scheduled', 'Scheduled'),
        ('now', 'Now'),
        ('completed', 'Completed'),
        ('missed', 'Missed'),
        ('paid', 'Paid'),

    ]
    group = models.ForeignKey(Group, related_name="lessonHistory", on_delete=models.CASCADE)
    tutor = models.ForeignKey(Tutor, related_name="lessonHistory", on_delete=models.CASCADE)
    dateTime = models.DateTimeField()
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='scheduled')
    comments = models.TextField()

    def __str__(self):
        return f"Group: {str(self.group)} - Tutor: {self.tutor} - {self.dateTime.strftime('%Y-%m-%d %H:%M')} - {self.get_status_display()}"

