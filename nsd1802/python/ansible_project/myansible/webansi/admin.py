# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from .models import Group, Host, Module, Args

admin.site.register(Group)
admin.site.register(Host)
admin.site.register(Module)
admin.site.register(Args)

