# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

class Group(models.Model):
    hostgroup = models.CharField(max_length=50)

    def __str__(self):
        return self.hostgroup

class Host(models.Model):
    hostname = models.CharField(max_length=50)
    ipaddr = models.CharField(max_length=15)
    group = models.ForeignKey(Group, on_delete=models.CASCADE)

    def __str__(self):
        return '<%s: %s>' % (self.hostname, self.ipaddr)

class Module(models.Model):
    module_name = models.CharField(max_length=50)

    def __str__(self):
        return self.module_name

class Args(models.Model):
    args_text = models.CharField(max_length=100)
    module = models.ForeignKey(Module, on_delete=models.CASCADE)

    def __str__(self):
        return self.args_text
