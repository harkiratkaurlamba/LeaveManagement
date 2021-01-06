from __future__ import unicode_literals
from django.db import models

# Create your models here.s
class todayOnLeave(models.Model):
    name = models.CharField(max_length = 300)
    day = models.IntegerField(blank=True, null=True)
    month = models.IntegerField(blank=True, null=True)
    

    def __str__(self):
        return self.name + " - " + str(self.day) + " - " + str(self.month)






