from django.contrib import admin
from .models import Trainer


@admin.register(Trainer)
class TrainerAdmin(admin.ModelAdmin):
	list_display = ('first_name', 'last_name', 'subject')
	ordering = ('last_name',)
	search_fields = ('first_name', 'last_name', 'subject')