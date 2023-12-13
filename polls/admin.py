from django.contrib import admin
from .models import Poll
# Register your models here.
@admin.register(Poll)
class PollAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug']
    prepopulated_fields = {'slug': ('name',)}


