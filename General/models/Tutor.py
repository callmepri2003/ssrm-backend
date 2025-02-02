from django.db import models
from django.contrib.auth.models import User

class Tutor(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.user.username

    # @property
    # def total_paid(self):
    #     total = 0
    #     for group in self.groups.all():
    #         total += group.cost
        
    #     return 40
