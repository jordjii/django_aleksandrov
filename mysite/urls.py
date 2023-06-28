

from django.conf.urls.static import static
from django.contrib import admin
from django.conf import settings
from django.contrib.auth.views import LogoutView, LoginView
from django.urls import path, include


urlpatterns = [
    path("admin/", admin.site.urls),
    path('blog/', include(('blog.urls', 'blog'))),
    path('logout/', LogoutView.as_view()),
    path('login/', LoginView.as_view()),
] + static(settings.STATIC_URL, document_root=settings.STATICFILES_DIRS)


