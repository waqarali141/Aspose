# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.


class Extension(models.Model):
    name = models.CharField(max_length=20, primary_key=True, unique=True)
    detail = models.TextField()
    prefix = models.CharField(max_length=120)

    def __str__(self):
        return self.name