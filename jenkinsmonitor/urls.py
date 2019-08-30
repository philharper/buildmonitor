from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('monitor/<monitor_id>', views.monitor, name='monitor'),
    path('create', views.create, name='create'),
    path('create/monitor', views.create_monitor, name='create_monitor'),
    path('delete/<monitor_id>', views.delete_monitor, name='delete_monitor'),
    path('edit/monitor/<monitor_id>', views.edit, name='edit'),
    path('edit/monitor', views.edit_monitor, name='edit_monitor'),
]
