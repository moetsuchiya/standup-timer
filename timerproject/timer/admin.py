from django.contrib import admin
from .models import StudyRecord, CategoryRecord, TitleRecord

admin.site.register(StudyRecord)
admin.site.register(CategoryRecord)
admin.site.register(TitleRecord)