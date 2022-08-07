from django.contrib import admin
from django.urls import path
from django.urls import include, path

urlpatterns = [
    path('admin/', admin.site.urls),
    # path('cysb/', include('cysb.urls')),
    path('cysb/', include('cysb.urls')),
    path('', include('team3pj.urls')),    
]