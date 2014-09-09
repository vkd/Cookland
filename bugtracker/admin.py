from django.contrib import admin
from .models import Ticket

class TicketAdmin(admin.ModelAdmin):
	list_display = ('closed', 'title', 'text', 'created', 'user')
	list_filter = ['created', 'closed']
	search_fields = ['title', 'text']

# Register your models here.
admin.site.register(Ticket, TicketAdmin)