
from django.db import models
from django.contrib.auth.models import User
from collections import defaultdict

class Student(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    join_date = models.DateTimeField()
    exit_date = models.DateTimeField(null=True, blank=True)


    def __str__(self):
        return str(self.user)
    
    @property
    def total_amount_spent(self):
        # Prefetch all related data in 2 optimized queries
        attendances = self.attendedLessons.select_related('lesson__group').prefetch_related('lesson__group__enrolments').filter(trial=False)
        enrolments = self.enrolments.select_related('group')
        
        # Create lookup dictionary for enrolment costs {group_id: [cost1, cost2...]}
        cost_map = defaultdict(list)
        for enrolment in enrolments:
            cost_map[enrolment.group.id].append(enrolment.enrolmentCost)
        
        # Calculate total using generator expression
        return sum(
            sum(cost_map[attendance.lesson.group.id])  # Sum all costs for this group
            for attendance in attendances.all()
        )

