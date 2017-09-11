# -*- coding: utf-8 -*-

from scrapy_djangoitem import DjangoItem

from extensions.models import Extension


# Django model item as Scrapy item
class AsposeTaskItem(DjangoItem):
    django_model = Extension
