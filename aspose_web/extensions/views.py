# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.views import generic

from .models import Extension


class ExtensionsPrefixes(generic.ListView):
    template_name = 'extensions/prefixes.html'
    context_object_name = 'prefixes'

    def get_queryset(self):
        return Extension.objects.values('prefix').distinct().order_by('prefix')


class ExtensionsNames(generic.ListView):
    template_name = 'extensions/names.html'
    context_object_name = 'prefix_names'
    paginate_by = 30

    def get_queryset(self):
        prefix_name = self.kwargs['prefix']
        return Extension.objects.filter(prefix=prefix_name).values_list('name', 'pk').order_by('name')


class ExtensionDetail(generic.DetailView):
    model = Extension
    template_name = 'extensions/detail.html'
    context_object_name = 'extension'
