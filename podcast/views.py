from django.shortcuts import render

def podcasts_list(request):
    return render(request, 'podcast/podcast_list.html', {})
