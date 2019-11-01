from django.conf.urls.static import static
from django.urls import path
from podcast import views

urlpatterns = [
    path('', views.podcasts_list, name="home_page"),
    path('<int:podcast_id>/', views.podcast_details, name='podcast_details'),
    path('<int:podcast_id>/comment/', views.add_comment_to_podcast, name='comment'),
]

