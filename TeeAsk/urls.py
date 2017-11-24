from django.conf.urls import url, include
from django.contrib import admin
from TeeAsk import views
from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf import settings

from TeeAsk.views import *

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', IndexView.as_view()),
    url(r'^login/', LoginView.as_view()),
    url(r'^logout/', LogoutView.as_view()),
    url(r'^like/', LiveView.as_view()),
    url(r'^new_question/', NewQuestionView.as_view()),
    url(r'^question/', QuestionView.as_view()),
    url(r'^settings/', SettingsView.as_view()),
] #+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)