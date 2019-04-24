from django.urls import path

from . import views

urlpatterns = [
    path('list', views.index, name='list'),
    path('monitor/<int:monitor_id>', views.monitor, name='monitor'),
]