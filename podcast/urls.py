from django.urls import path

from podcast import views

urlpatterns = [
    path('podcasts/', views.podcasts_list),
    ]