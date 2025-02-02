from django.db import models

from General.models.Group import Group

class Resource(models.Model):
    group = models.ForeignKey(Group, related_name="resources", on_delete=models.PROTECT)
    file = models.FileField(upload_to="")
    title = models.CharField(max_length=20)
    
