from django.urls import path

from . import views

app_name = 'report'

urlpatterns = [
    path('', views.index, name='index'),
    path('report_add/', views.report_add, name='report_add'),
    # path('report/<int:pk>/', views.report_detail, name='report_detail'),
    path('report/<int:pk>/edit/', views.report_edit, name='report_edit'),
    path('report/<int:pk>/delete/', views.report_delete, name='report_delete'),
    path('export/xls/', views.export_xls, name='export_xls'),
]