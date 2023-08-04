from django.urls import path, include
from . import views

app_name = 'boards'

urlpatterns = [
    path("", views.index, name='index'),
    path("write/", views.write, name='write'),
    path("<int:question_id>/", views.detail, name='detail'),
    path("<int:question_id>/edit/", views.edit, name="edit"),
    path("<int:question_id>/delete/", views.delete, name="delete"),
]
