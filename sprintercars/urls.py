from django.conf.urls import url
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path

from sprintercars import settings

urlpatterns = [
    path('grappelli/', include('grappelli.urls')),
    url(r'^admin/', admin.site.urls),
    url(r'', include('sprintercarsapp.urls')),
    url(r'^ckeditor/', include('ckeditor_uploader.urls')),
]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
# admin.site.site_header = 'Sprinter Cars'
