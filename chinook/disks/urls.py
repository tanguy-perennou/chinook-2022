from django.urls import path

from . import views

app_name = 'disks'
urlpatterns = [
    # ex: /disks/
    path('', views.albums_list, name='albums_list'),
    # ex: /disks/5/
    path('<int:album_id>/', views.album_details, name='album_details'),
    path('artist/create/', views.create_artist, name='create_artist'),
    path('artist/update/<int:artist_id>/', views.update_artist, name='update_artist')
]