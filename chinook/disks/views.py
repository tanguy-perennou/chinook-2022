from django.http import HttpResponse
from django.shortcuts import get_list_or_404, get_object_or_404, render

from .models import Album


def albums_list(request):
    albums = get_list_or_404(Album)
    return render(request, 'disks/albums_list.html', {'albums': albums})


def album_details(request, album_id):
    album = get_object_or_404(Album, pk=album_id)
    return render(request, 'disks/album_details.html', {'album': album})
