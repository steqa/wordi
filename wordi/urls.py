from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('cards.urls')),
    path('account/', include('accounts.urls')),
    path('userprofile/', include('userprofile.urls')),
    path('lesson/', include('lesson.urls')),
    path('statistics/', include('stats.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
