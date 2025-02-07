from django.contrib import admin
from .models import MissingPerson

@admin.register(MissingPerson)
class MissingPersonAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'age', 'last_seen_location', 'reported_at')
    # list_display = ('id', 'name', 'age', 'last_seen_location', 'created_by', 'reported_at','username')
    search_fields = ('name', 'last_seen_location')
    list_filter = ('reported_at',)

