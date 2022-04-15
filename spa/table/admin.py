from django.contrib import admin
from .models import Table


class TableAdmin(admin.ModelAdmin):
    fields = ('date', 'name', 'count', 'distance')


admin.site.register(Table, TableAdmin)
