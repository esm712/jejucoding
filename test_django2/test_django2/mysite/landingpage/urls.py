from django.contrib import admin
from django.urls import path
from main.views import index #views.py에 index라는 함수 매칭 
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',index),
]

urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)