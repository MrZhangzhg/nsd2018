from django.contrib import admin
from .models import HostGroup, Host, AnsiModule, ModuleArg

for item in [ HostGroup, Host, AnsiModule, ModuleArg]:
    admin.site.register(item)
