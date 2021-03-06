from django.urls import path

from . import views

app_name = 'logs'

urlpatterns = [
    path('', views.index, name='index'),
    path('tasks/', views.tasks, name='tasks'),
    path('tasks/performed/<int:id>/', views.performed),
    path('tasks/add-task/', views.add_task),
    path('change-gpio/', views.change_gpio, name='change_gpio'),
    path('state-gpio/', views.state_gpio, name='state_gpio'),
    path('video_feed/', views.video_feed),
    # path('webcam_feed', views.webcam_feed, name='webcam_feed'),
	# path('livecam_feed', views.livecam_feed, name='livecam_feed'),

]
