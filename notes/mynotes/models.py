from django.contrib.auth.models import User
from django.urls import reverse
from django.db import models

# class Us(models.Model):
#     us_name = models.CharField(max_length=150, db_index = True)

#     def __str__(self):
#         return self.us_name

class Notes(models.Model):
    title = models.CharField(max_length = 100)
    note_text = models.TextField()
    date = models.DateTimeField(auto_now = True)
    user = models.ForeignKey(User, on_delete = models.CASCADE, null = True)

    def __str__(self):
        return self.title
