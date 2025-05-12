from django.db import models
from datetime import timedelta
# Create your models here.
CATEGORY = (('English', '英語'), ('ComputerScience', '情報'))

class DurationChoices(models.Model):
    name = models.CharField(max_length=50)
    duration = models.DurationField()

    def __str__(self):
        return self.name

class StudyRecord(models.Model):
    title = models.CharField(max_length=100)
    descrition = models.TextField(null=True, blank=True)
    start_time = models.DateTimeField(auto_now_add=True, verbose_name="日時")
    duration = models.ForeignKey(
        DurationChoices,
        on_delete=models.CASCADE,
        verbose_name="作業時間")
    category = models.CharField(
        verbose_name='カテゴリ',
        max_length=100,
        choices = CATEGORY
    )

    #userを登録

    def __str__(self):
        return self.title