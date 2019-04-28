from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('jenkins/', include(('jenkinsmonitor.urls', 'jenkinsmonitor'), namespace='jenkinsmonitor')),
    path('admin/', admin.site.urls),
]
