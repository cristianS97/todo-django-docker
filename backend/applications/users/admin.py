from django.contrib import admin
from .models import User

# Register your models here.
class UserAdmin(admin.ModelAdmin):
    list_display = ('email', 'names', 'last_name')
    list_display_links = ('email', 'names', 'last_name')
    search_fields = ('email', 'ocupation', 'names', 'last_name')
    list_filter = ('email', 'birth_date')
    readonly_fields = ('created', 'updated')

admin.site.register(User, UserAdmin)
