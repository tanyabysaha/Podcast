from django.conf.urls.static import static
from django.urls import path

from mysite import settings
from podcast import views

urlpatterns = [
    path('', views.podcasts_list),
    ]