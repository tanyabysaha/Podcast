from django.urls import path

from podcast import views

urlpatterns = [
    path('', views.podcasts_list),
    ]