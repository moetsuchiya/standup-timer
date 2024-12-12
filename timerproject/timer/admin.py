from django.contrib import admin
from .models import StudyRecord, DurationChoices

admin.site.register(StudyRecord)

admin.site.register(DurationChoices)
class DurationChoicesAdmin(admin.ModelAdmin):
    list_display = ("name", "duration")