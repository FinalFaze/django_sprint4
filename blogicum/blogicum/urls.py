from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path

from blog import views as blog_views
from pages.views import logout_get  # <-- ВОТ ТУТ, ВМЕСТЕ С ИМПОРТАМИ

urlpatterns = [
    path('admin/', admin.site.urls),

    # регистрация (как было)
    path('auth/registration/', blog_views.RegistrationView.as_view(), name='registration'),

    # logout по GET (чтобы ссылка в шаблоне работала)
    path('auth/logout/', logout_get, name='logout'),

    # остальная auth-часть
    path('auth/', include('django.contrib.auth.urls')),

    # приложения
    path('', include('blog.urls')),
    path('', include('pages.urls')),
]

handler404 = 'pages.views.page_not_found'
handler500 = 'pages.views.server_error'
handler403 = 'pages.views.permission_denied'

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
