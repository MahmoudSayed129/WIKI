from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("wiki/<str:title>", views.get_page, name="get_page"),
    path("random", views.get_random, name="get_random"),
    path("newpage", views.newpage, name="newpage"),
    path("search", views.search, name="search"),
    path("add", views.add, name="add"),
    path("edit", views.edit, name="edit"),
    path("save_edit", views.save_edit, name="save_edit")
]
