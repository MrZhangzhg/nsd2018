from django.contrib import admin
from .models import Host, HostGroup, AnsibleModule, ModuleArg

for item in [Host, HostGroup, AnsibleModule, ModuleArg]:
    admin.site.register(item)
