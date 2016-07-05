from __future__ import unicode_literals
from django.db import models


class Post(models.Model):
    name = models.CharField(max_length=128)
    email = models.EmailField()
    comment = models.TextField()
  #  box = models.BooleanField()

    def __unicode__(self):
        return self.title

    def _str_(self):
        return self.title

# class User(models.Model):
#     name = models.CharField(max_length=50)
#     email = models.EmailField()
#     comment = models.CharField(max_length=500)
#

