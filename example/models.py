from django.db import models

# Create your models here.

class Example(models.Model):
    field1 = models.CharField(max_length=5, default="xxx")
    field2 = models.CharField(max_length=23, null=True, blank=True)
    field3 = models.BooleanField(default=False)
    field4 = models.IntegerField(default=42)
    field5 = models.TextField(null=True, blank=True)
