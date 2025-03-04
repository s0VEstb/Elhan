
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from Elhan import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('post/', include('post.urls')),
    path('user/', include('user.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
