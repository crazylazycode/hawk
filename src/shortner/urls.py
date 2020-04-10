
from django.contrib import admin
from django.urls import path,re_path

from urlshortner.views import HomeView,URLRediectView

urlpatterns = [
    path('admin/', admin.site.urls),
    re_path(r'^$',HomeView.as_view()),
    re_path(r'^(?P<shortcode>[\w-]+)/$',URLRediectView.as_view(),name='scode'),
]
