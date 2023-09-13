from django.contrib import admin
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('home/', include(('aviaweb.urls', 'aviaweb'), namespace='aviaweb')),
    path('users/', include(('users.urls', 'users'), namespace='users'))
    ]
