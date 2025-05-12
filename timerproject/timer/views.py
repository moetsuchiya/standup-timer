from .models import CategoryRecord, TitleRecord, StudyRecord
from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView, CreateView, DeleteView, UpdateView, TemplateView
from django.urls import reverse_lazy
from django.contrib.auth import logout
from django.http import JsonResponse
import json
from datetime import timedelta, datetime
from django.utils import timezone
import numpy as np
import pandas as pd
from django_pandas.io import read_frame
from .plugin_plotly import GraphGenerator
from django import template
#コマンド打つときにtabキーを押すとpath書ける

class ListTimerView(ListView):
    template_name = 'timer/timer_list.html'
    model = StudyRecord

class DetailTimerView(DetailView):
    template_name = 'timer/timer_detail.html'
    model = StudyRecord

class DeleteTimerView(DeleteView):
    template_name = 'timer/timer_delete.html'
    model = StudyRecord
    success_url = reverse_lazy('list-timer')

class CreateCategoryView(CreateView):
    template_name = 'timer/timer_create_category.html'
    model = CategoryRecord
    fields = ('category',)
    success_url = reverse_lazy('create-title')

class CreateTitleView(CreateView):
    template_name = 'timer/timer_create_title.html'
    model = TitleRecord
    fields = ('category','title')
    success_url = reverse_lazy('clock')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categories'] = CategoryRecord.objects.all()
        print(context)
        return context

class ListCategoryView(ListView):
    template_name = 'timer//timer_list_category.html'
    model = CategoryRecord

class ListTitleView(ListView):
    template_name = 'timer//timer_list_title.html'
    model = TitleRecord

class DeleteCategoryView(DeleteView):
    template_name = 'timer/timer_delete_category.html'
    model = CategoryRecord
    success_url = reverse_lazy('list-category')

class DeleteTitleView(DeleteView):
    template_name = 'timer/timer_delete_title.html'
    model = TitleRecord
    success_url = reverse_lazy('list-title')

class UpdateTimerView(UpdateView):
    template_name = 'timer/timer_update.html'
    model = StudyRecord
    fields = ('title', 'description')
    success_url = reverse_lazy('list-timer')

def index_view(request):
    object_list = StudyRecord.objects.all().order_by('category')
    return render(request, 'timer/index.html', {'object_list': object_list})

def logout_view(request):
    logout(request)
    return redirect('index')

def clock_view(request):
    if request.method == "GET":
        categories = CategoryRecord.objects.all()
        titles = TitleRecord.objects.all()
        return render(request, 'timer/timer_clock.html', {
            'categories': categories,
            'titles': titles,
        })

    elif request.method == "POST":
        try:
            data = json.loads(request.body)
            elapsed_seconds = data.get("elapsed_time", 0)
            title_id = data.get("title_id")  # タイトルIDのみ取得

            elapsed_time = timedelta(seconds=elapsed_seconds)

            # タイトルのレコードのみを取得
            title = TitleRecord.objects.get(id=title_id)

            # StudyRecordに保存
            StudyRecord.objects.create(
                title=title,
                start_time=timezone.now(),
                duration=elapsed_time
            )
            return JsonResponse({"message": "記録しました"}, status=200)

        except TitleRecord.DoesNotExist:
            return JsonResponse({"error": "無効なタイトルが選択されました"}, status=400)
        except json.JSONDecodeError:
            return JsonResponse({"error": "無効なJSONデータです"}, status=400)

    return JsonResponse({"error": "無効なリクエスト"}, status=400)

class DashboardView(TemplateView):
    template_name = 'timer/timer_dashboard.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        # フィルタリングを削除し、全データを取得
        queryset = StudyRecord.objects.all()

        # デバッグ用のprint
        print("データ件数:", queryset.count())
        print("クエリセット:", queryset.values())

        # クエリセットが空の場合は早期リターン
        if not queryset.exists():
            print("データが存在しません")
            return context

        # クエリセットをpandasのDataFrameに変換
        df = read_frame(
            queryset,
            fieldnames=['title', 'duration', 'start_time'],
            verbose=True
        )

        # titleオブジェクトから直接カテゴリを取得
        def get_category(title_name):
            title_obj = TitleRecord.objects.get(title=title_name)
            return title_obj.category.category

        # 作業時間（秒）を計算して列を追加
        df['category'] = df['title'].apply(get_category)
        df['duration_seconds'] = df['duration'].dt.total_seconds()

        # カテゴリ別の合計作業時間を集計（円グラフ用）
        df_pie = pd.pivot_table(df, index='category', values='duration_seconds', aggfunc=np.sum)
        pie_labels = list(df_pie.index.values)
        pie_values = [float(duration_value[0]) for duration_value in df_pie.values] #[[3.], [1.], [1.]]

        gen = GraphGenerator()
        plot_pie = gen.month_pie(labels=pie_labels, values=pie_values)
        context['plot_pie'] = plot_pie

        # カテゴリ別の合計時間を辞書形式で保存（テーブル用）
        table_set = df_pie.to_dict()['duration_seconds']
        context['table_set'] = {k: float(v) for k, v in table_set.items()}

        # 合計作業時間を計算
        context['total_duration'] = float(df['duration_seconds'].sum())

        # 日別の作業時間を集計（棒グラフ用）
        df_bar = pd.pivot_table(df, index=df['start_time'].dt.date, values='duration_seconds', aggfunc=np.sum)
        dates = list(df_bar.index.values)
        durations = [val[0] for val in df_bar.values]
        plot_bar = gen.month_daily_bar(x_list=dates, y_list=durations)
        context['plot_bar'] = plot_bar

        return context
