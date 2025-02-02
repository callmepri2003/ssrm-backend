from django.db import models

from General.models.Group import Group
from General.models.Student import Student
from django.utils import timezone

class Reporting(models.Model):
    UNIQUE = [
        ('u', 'UNIQUE'),
    ]

    unique = models.CharField(max_length=6, choices=UNIQUE, default='u', unique=True)

    class Meta:
        verbose_name = "Reporting"
        verbose_name_plural = "Reportings"  # Optionally, specify the plural form for the model
    
    @property
    def totalEstimatedWeeklyProfit(self):
        groups = Group.objects.all()
        total = 0.00
        for group in groups:
            total += group.estimatedProfit
        return total
    
    @property
    def totalEnrolled(self):
        return Student.objects.filter(exit_date__isnull=True).count()

    from django.utils import timezone

    @property
    def averageLifetime(self):
        # Get all students
        students = Student.objects.all()
        
        # Initialize total duration and count of students
        total_duration = 0
        enrolled_count = 0
        
        for student in students:
            # If exit date is null, assume the student is still enrolled and use today's date
            exit_date = student.exit_date if student.exit_date else timezone.now()
            
            # Calculate the duration
            duration = exit_date - student.join_date
            
            # Accumulate the duration and increase the count
            total_duration += duration.days/28
            enrolled_count += 1
        
        # If no students are found, avoid division by zero
        if enrolled_count == 0:
            return 0
        
        # Return the average duration
        return f"{total_duration / enrolled_count:.2} months"


