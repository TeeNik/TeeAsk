from django.conf.urls import url, include
from django.contrib import admin
from TeeAsk import views
from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf import settings

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', views.index),
    url(r'^login/', views.login_page),
    url(r'^logout/', views.logout_page),
    url(r'^like/', views.like),
    url(r'^new_question/', views.new_question),
    url(r'^question/', views.question),
    url(r'^settings/', views.settings),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)