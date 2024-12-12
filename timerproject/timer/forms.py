from django import forms
from django.contrib import admin
from .models import StudyRecord, DurationChoices

class StudyRecordForm(forms.ModelForm):
    duration = forms.ModelChoiceField(
        queryset=DurationChoices.objects.all(),
        label="作業時間",
        help_text="選択肢から作業時間を選んでください。",
    )

    class Meta:
        model = StudyRecord
        fields = "__all__"

@admin.register(StudyRecord)
class StudyRecordAdmin(admin.ModelAdmin):
    form = StudyRecordForm
