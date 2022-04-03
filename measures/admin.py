from django.contrib import admin

from measures.models import Measure

@admin.register(Measure)
class MeasureAdmin(admin.ModelAdmin):
    list_display = ('name',)
