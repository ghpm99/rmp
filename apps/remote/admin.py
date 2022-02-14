from django.contrib import admin
from remote.models import Config


# Register your models here.
class ConfigAdmin(admin.ModelAdmin):
    pass


admin.site.register(Config, ConfigAdmin)
