from django.db import models

class HostGroup(models.Model):
    group_name = models.CharField(max_length=30, unique=True)

    def __str__(self):
        return self.group_name

class Host(models.Model):
    hostname = models.CharField(max_length=50, unique=True)
    ipaddr = models.CharField(max_length=15)
    hostgroup = models.ForeignKey(HostGroup, on_delete=models.CASCADE)

    def __str__(self):
        return "<%s: %s>" % (self.hostname, self.ipaddr)

class AnsibleModule(models.Model):
    mod_name = models.CharField(max_length=30)

    def __str__(self):
        return self.mod_name

class ModuleArg(models.Model):
    arg_text = models.CharField(max_length=100)
    mod = models.ForeignKey(AnsibleModule, on_delete=models.CASCADE)

    def __str__(self):
        return self.arg_text
