from django.db import models

class HostGroup(models.Model):
    hostgroup = models.CharField(max_length=20, unique=True)

    def __str__(self):
        return self.hostgroup

class Host(models.Model):
    hostname = models.CharField(max_length=50, unique=True)
    ipaddr = models.CharField(max_length=15, unique=True)
    group = models.ForeignKey(HostGroup, on_delete=models.CASCADE)

    def __str__(self):
        return "<%s -> %s>" % (self.hostname, self.group)

class AnsiModule(models.Model):
    mod_name = models.CharField(max_length=30)

    def __str__(self):
        return self.mod_name

class ModArgs(models.Model):
    args_text = models.CharField(max_length=100)
    mod = models.ForeignKey(AnsiModule, on_delete=models.CASCADE)

    def __str__(self):
        return "<%s -> %s>" % (self.args_text, self.mod)
