# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy
from scrapy_djangoitem import DjangoItem
# -*- coding: utf-8 -*-

from extensions.models import Extension
# from django.db import models
# class Extension(models.Model):
#     name = models.CharField(max_length=20)
#     detail = models.TextField()
#     prefix = models.CharField(max_length=120)
#
#     def __str__(self):
#         return self.name

class AsposeTaskItem(DjangoItem):
    django_model = Extension


