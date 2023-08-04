from django.urls import path, include
from . import views

app_name = 'boards'

urlpatterns = [
    path("", views.index, name='index'),
    path("write/", views.write, name='write'),
    path("<int:post_id>/", views.detail, name='detail'),
    path("<int:post_id>/edit/", views.edit, name="edit"),
    path("<int:post_id>/delete/", views.delete, name="delete"),
]
