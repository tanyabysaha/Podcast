from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.db.models import Q
from django.http import Http404
from django.shortcuts import render, get_object_or_404, redirect
from django.utils.crypto import random
from podcast.models import Podcast
from podcast.models import Comment


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

def podcast_details(request, podcast_id):
    specific_podcast = Podcast.objects.filter(id=podcast_id).first()
    podcasts = Podcast.objects.all()
    random_podcasts = random.sample(list(podcasts), 2)

    query = request.GET.get("q")

    if query:
        podcasts = Podcast.objects.filter(Q(pod_title__icontains=query) | Q(description__icontains=query))
    if not specific_podcast:
        raise Http404

    return render(request, 'podcast/podcast_details.html', {"specific_podcast": specific_podcast, "podcasts": podcasts, "random_podcasts": random_podcasts})

def add_comment_to_podcast(request, podcast_id):
    podcast = get_object_or_404(Podcast, id=podcast_id)
    if request.method == "POST":
        print(request.POST)
        Comment.objects.create(user=request.POST.get("user"), comment_text=request.POST.get("comment_text"), podcast=podcast)

    return redirect("podcast_details", podcast_id=podcast.id)


