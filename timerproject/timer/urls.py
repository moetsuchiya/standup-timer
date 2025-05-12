from django.urls import path
from . import views

urlpatterns = [
    path('', views.clock_view, name='index'),
    path('logout/', views.logout_view, name='logout'),
    path('clock/', views.clock_view, name='clock'),
    path('timer/timer_dashboard/', views.DashboardView.as_view(), name='dashboard-timer'),
    path('timer/list/', views.ListTimerView.as_view(), name='list-timer'),
    path('timer/<int:pk>/', views.DetailTimerView.as_view(), name='detail-timer'),
    path('timer/<int:pk>/delete/', views.DeleteTimerView.as_view(), name='delete-timer'),
    path('timer/<int:pk>/update/', views.UpdateTimerView.as_view(), name='update-timer'),
    path('category/create/', views.CreateCategoryView.as_view(), name='create-category'),
    path('title/create/', views.CreateTitleView.as_view(), name='create-title'),
    path('category/list/', views.ListCategoryView.as_view(), name='list-category'),
    path('title/list/', views.ListTitleView.as_view(), name='list-title'),
    path('category/<int:pk>/delete/', views.DeleteCategoryView.as_view(), name='delete-category'),
    path('title/<int:pk>/delete/', views.DeleteTitleView.as_view(), name='delete-title'),
]