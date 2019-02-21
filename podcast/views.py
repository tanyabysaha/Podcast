from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.db.models import Q
from django.shortcuts import render
from podcast.models import Podcast




def podcasts_list(request):

    podcasts = Podcast.objects.all()
    query = request.GET.get("q")
    if query:
        podcasts = Podcast.objects.filter(Q(pod_title__icontains=query) | Q(description__icontains=query))
    paginator = Paginator(podcasts, 4)
    page = request.GET.get('page')

    try:
        podcasts = paginator.page(page)
    except PageNotAnInteger:
        podcasts = paginator.page(1)
    except EmptyPage:
        podcasts = paginator.page(paginator.num_pages)

    index = podcasts.number - 1
    max_index = len(paginator.page_range)
    start_index = index - 3 if index >= 3 else 0
    end_index = index + 3 if index <= max_index - 3 else max_index
    page_range = paginator.page_range[start_index:end_index]




    return render(request, 'podcast/podcast_list.html', {"podcasts": podcasts, "page_range": page_range})


