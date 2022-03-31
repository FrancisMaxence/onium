from django.contrib import admin

from onium.measure.models import Measure

@admin.register(Measure)
class MeasureAdmin(admin.ModelAdmin):
    list_display = ('name',)
