from django.contrib import admin
from .models import Trainer


admin.site.site_header = 'Trainer adminstration'
admin.site.index_title = 'Trainer'
admin.site.site_title = 'Trainer site admin'


@admin.register(Trainer)
class TrainerAdmin(admin.ModelAdmin):
	list_filter = ('first_name', 'last_name')
	list_display = ('first_name', 'last_name', 'subject')
	ordering = ('last_name',)
	search_fields = ('first_name', 'last_name', 'subject')
