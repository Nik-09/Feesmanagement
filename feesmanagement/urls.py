from django.urls import path

from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('classroom-summary', views.classroomSummary, name='classroomSummary'),
    path('fees-record-form', views.feesRecordFormPage, name='feesRecordFormpage'),
    path('monthly-stats', views.monthlyStatsPage, name='monthlyStatsPage'),
]