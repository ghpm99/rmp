from django.contrib import admin
from media_socket.models import Event


# Register your models here.
class Events(admin.ModelAdmin):
    list_display = ('id', 'event')
    list_display_links = ('id', 'event')
    search_fields = ('id',)
    list_per_page = 20


admin.site.register(Event, Events)
