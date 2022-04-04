from django.shortcuts import get_list_or_404, get_object_or_404, render

from .forms import SearchForm
from .models import Album


def albums_list(request):
    """
    Get albums from database, either all of them or those matching a POST request
    :param request: The incoming request
    """
    if request.method == 'POST':
        form = SearchForm(request.POST)
        if form.is_valid():
            query = form.cleaned_data['query']
            albums = Album.objects.filter(title__icontains=query)
            # using HttpResponseRedirect is not appropriate here: albums must be rendered
        else:
            albums = get_list_or_404(Album)
    else:
        form = SearchForm()
        albums = get_list_or_404(Album)
    return render(request, 'disks/albums_list.html', {'albums': albums, 'form': form})


def album_details(request, album_id):
    """
    Get the specified album
    :param request: The incoming request
    :param album_id: The album's ID
    """
    album = get_object_or_404(Album, pk=album_id)
    return render(request, 'disks/album_details.html', {'album': album})
