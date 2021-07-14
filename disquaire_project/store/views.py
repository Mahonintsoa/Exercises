from django.shortcuts import render, get_object_or_404
from .models import Album, Artist, Contact, Booking
from .forms import SearchForm
from django.contrib.postgres.search import SearchQuery, SearchRank


# Create your views here.
def index(request):
    albums = Album.objects.filter(available=True).order_by('created_at')[:3]
    return render(request, 'index.html', {'albums': albums})


def listing(request):
    albums = Album.objects.filter(available=True)[:6]
    context = {
        'albums': albums,
    }
    return render(request, 'store/list.html', context)


def detail(request, id):
    album = get_object_or_404(Album, id=id)
    artists = " ".join([artist.name for artist in album.artiste.all()])
    context = {
        'album_title': album.title,
        'artists': artists,
        'album_id': album.id,
        'thumbnail': album.picture,
    }
    return render(request, 'store/detail.html', context)


def search(request):
    form = SearchForm()
    query = None
    results = []
    if 'query' in request.GET:
        form = SearchForm(request.GET)
        if form.is_valid():
            query = form.cleaned_data['query']
            search_query = SearchQuery(query)
            results = Album.annotate(rank=SearchRank(search_query))

    context = {
        'form': form,
        'query': query,
        'results': results,
    }
    return render(request, 'store/search.html', context)
