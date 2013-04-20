from django.db import models

# Create your models here.

class ClickMe(models.Model):
    dateCreated = models.DateTimeField(auto_now=True)


