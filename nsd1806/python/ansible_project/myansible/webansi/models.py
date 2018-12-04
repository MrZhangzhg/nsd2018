from django.db import models

class HostGroup(models.Model):
    groupname = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.groupname

class Host(models.Model):
    hostname = models.CharField(max_length=50, unique=True)
    ipaddr = models.CharField(max_length=15)
    group = models.ForeignKey(HostGroup, on_delete=models.CASCADE)

    def __str__(self):
        return "<%s->%s>" % (self.hostname, self.group)

class AnsiModule(models.Model):
    module_name = models.CharField(max_length=30, unique=True)

    def __str__(self):
        return self.module_name

class ModuleArg(models.Model):
    arg_text = models.CharField(max_length=100)
    mod = models.ForeignKey(AnsiModule, on_delete=models.CASCADE)

    def __str__(self):
        return "<%s->%s>" % (self.arg_text, self.mod)
