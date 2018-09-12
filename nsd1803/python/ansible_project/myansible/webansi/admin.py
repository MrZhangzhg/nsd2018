# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from .models import Host, Group, Module, Args

for item in [Group, Host, Module, Args]:
    admin.site.register(item)
