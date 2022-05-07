from django.contrib import admin
from main.models import *
from django.utils.html import format_html

# Register your models here.
@admin.action(description="Reset access counts")
def reset_access_count(modeladmin, request, queryset):
    queryset.update(shortcut_accesses = 0)

class shortcutAdmin(admin.ModelAdmin):
    actions = [reset_access_count]
    list_display = ('shortcut_key','shortcut_value', 'shortcut_accesses', 'show_logs_url')
    list_display_links = ('shortcut_key', )
    def show_logs_url(self,obj):
        return format_html('<a href="/admin/main/log/?log_shortcut={}">Access Log</a>&nbsp;',obj.shortcut_key)
    show_logs_url.short_description = "Log"
    show_logs_url.allow_tags = True

class logAdmin(admin.ModelAdmin):
    list_filter = ('log_ip','log_shortcut')
    list_display = ('log_time','log_ip', 'log_ua', 'log_shortcut')
    list_display_links = ()
    def has_change_permission(self, request, obj=None):
        return False

admin.site.register(shortcut,shortcutAdmin)
admin.site.register(log,logAdmin) # /admin/main/log/?log_shortcut=test

admin.site.site_header = "Shortcuts Management Panel"
admin.site.site_title = "Shortcuts"
