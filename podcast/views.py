from django.shortcuts import render

from podcast.models import Podcast


def podcasts_list(request):
    podcasts = Podcast.objects.all()
    return render(request, 'podcast/podcast_list.html', {"podcasts": podcasts})
