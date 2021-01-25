from django.contrib import admin
from django.urls import path, include
from django.conf import settings #追加
from django.conf.urls.static import static #追加

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('blogapp.urls')),
]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) #追加
