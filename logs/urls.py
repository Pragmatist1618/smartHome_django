from django.urls import path

from . import views

app_name = 'logs'

urlpatterns = [
    path('', views.record_log, name='record-log'),
    path('topics/<int:topic_id>/', views.topic, name='topic'),
]
