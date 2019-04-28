from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('monitor/<monitor_id>', views.monitor, name='monitor'),
    path('create', views.create, name='create'),
    path('create/monitor', views.create_monitor, name='create_monitor'),
]
