from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path

from blog import views as blog_views

urlpatterns = [
    path('admin/', admin.site.urls),

    # пользователи
    path('auth/registration/', blog_views.RegistrationView.as_view(), name='registration'),
    path('auth/', include('django.contrib.auth.urls')),

    # приложения
    path('', include('blog.urls')),
    path('', include('pages.urls')),
]

handler403 = 'pages.views.permission_denied'
handler404 = 'pages.views.page_not_found'
handler500 = 'pages.views.server_error'

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
