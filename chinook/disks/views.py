from django.http import HttpResponse


def albums_list(request):
    return HttpResponse("List of albums here soon.")


def album_details(request, album_id):
    return HttpResponse("You're looking at album %s." % album_id)
