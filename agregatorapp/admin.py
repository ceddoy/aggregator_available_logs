from django.contrib import admin

from agregatorapp.models import Log


class LogAdmin(admin.ModelAdmin):
    list_display = ('ip_address', 'date_add')


admin.site.register(Log, LogAdmin)
