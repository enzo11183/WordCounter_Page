from django.db import models

# Create your models here.
class People(models.Model):
    age = models.IntegerField()
    name = models.CharField(max_length=80)

    def __str__(self):
        return self.name