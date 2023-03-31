from django.db import models

class File(models.Model):
    file_name = models.CharField(max_length=255)
    created_on = models.DateTimeField(auto_now_add=True)
