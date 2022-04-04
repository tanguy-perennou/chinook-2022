from django.urls import path

from . import views

app_name = 'disks'
urlpatterns = [
    # ex: /disks/
    path('', views.albums_list, name='albums_list'),
    # ex: /disks/5/
    path('<int:album_id>/', views.album_details, name='album_details')
]