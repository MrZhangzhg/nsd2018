from django.contrib import admin
from .models import HostGroup, Host, AnsiModule, ModArgs

class HostAdmin(admin.ModelAdmin):
    list_display = ('hostname', 'ipaddr', 'group')
    search_fields = ('hostname', 'ipaddr')
    # 用在有外键的项目上，创建主机时，可以显示组的详细信息
    raw_id_fields = ('group',)

class HostGroupAdmin(admin.ModelAdmin):
    search_fields = ('hostgroup', )

admin.site.register(Host, HostAdmin)
admin.site.register(HostGroup, HostGroupAdmin)

for item in [AnsiModule, ModArgs]:
    admin.site.register(item)

