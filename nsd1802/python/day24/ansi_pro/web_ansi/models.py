# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

class Hosts(models.Model):
    host = models.CharField(max_length=20)
    group = models.CharField(max_length=20)

    def __str__(self):
        return "[%s in %s]" % (self.host, self.group)

class Modules(models.Model):
    module_name = models.CharField(max_length=20)

class Args(models.Model):
    module = models.ForeignKey(Modules)
    args = models.CharField(max_length=100)
