from django.db import models

class users(models.Model):
    name = models.CharField(max_length=100, null=True)
    age = models.CharField(max_length=100, null=True)
    date_created = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return self.name