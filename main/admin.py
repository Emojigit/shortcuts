from django.contrib import admin
from main.models import *

# Register your models here.
@admin.action(description="Reset access counts")
def reset_access_count(modeladmin, request, queryset):
    queryset.update(shortcut_accesses = 0)

class shortcutAdmin(admin.ModelAdmin):
    actions = [reset_access_count]

admin.site.register(shortcut,shortcutAdmin)
admin.site.register(log)

admin.site.site_header = "Shortcuts Management Panel"
admin.site.site_title = "Shortcuts"
