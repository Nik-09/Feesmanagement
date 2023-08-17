from django.urls import path

from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('classroom-summary', views.classroomSummary, name='classroomSummary'),
    path('classroom-summary-form', views.classroomSummaryForm, name='classroomSummaryForm'),
    path('fees-record-form', views.feesRecordFormPage, name='feesRecordFormpage'),
    path('monthly-stats', views.monthlyStatsPage, name='monthlyStatsPage'),
    path('login', views.login, name='login'),
    path('logout', views.logout, name='logout'),
]