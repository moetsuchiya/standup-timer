from django.db import models

class CategoryRecord(models.Model):
    category = models.CharField(max_length=100, verbose_name="カテゴリ")
    def __str__(self):
        return self.category

class TitleRecord(models.Model):
    title = models.CharField(max_length=100, verbose_name="タスク名")
    category = models.ForeignKey(CategoryRecord, on_delete=models.CASCADE)
    def __str__(self):
        return self.title

class StudyRecord(models.Model):
    title = models.ForeignKey(TitleRecord, on_delete=models.CASCADE)
    description = models.TextField(null=True, blank=True, verbose_name="メモ")
    start_time = models.DateTimeField(verbose_name="日時")
    duration = models.DurationField(verbose_name="作業時間")