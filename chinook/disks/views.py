from django.shortcuts import get_list_or_404, get_object_or_404, render, redirect

from .forms import SearchForm, ArtistForm
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


def create_artist(request):
    """
    Create a new artist bases on user input in form

    Args:
        request: the incoming request, GET or POST

    Returns:
        - a page with an empty form if it was a GET request,
        - a page with an empty form if it was a POST request
          with invalid data,
        - or the list of albums if it was a POST with valid data
    """
    if request.method == 'GET':
        form = ArtistForm()
    elif request.method == 'POST':
        form = ArtistForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('disks:albums_list')
    return render(request, 'disks/create_artist.html', {'form': form})
