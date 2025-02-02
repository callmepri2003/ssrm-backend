from django.db import models
from django.contrib.auth.models import User

class Availability(models.Model):
    DAY_CHOICES = [
        ('monday', 'Monday'),
        ('tuesday', 'Tuesday'),
        ('wednesday', 'Wednesday'),
        ('thursday', 'Thursday'),
        ('friday', 'Friday'),
        ('saturday', 'Saturday'),
        ('sunday', 'Sunday'),
    ]
    
    tutor = models.ForeignKey('Tutor', related_name="availabilities", on_delete=models.CASCADE)
    day = models.CharField(max_length=9, choices=DAY_CHOICES)
    start_time = models.TimeField(null=True, blank=True)
    end_time = models.TimeField(null=True, blank=True)

    def __str__(self):
        return f"Availability for {self.tutor.user.username} on {self.get_day_display()}"

    class Meta:
        verbose_name_plural = "Availabilities"
        unique_together = ('tutor', 'day')  # Ensures one availability per day per tutor

