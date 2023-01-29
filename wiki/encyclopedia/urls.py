from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("new_page/", views.new_page, name="new_page"),
    path("wiki/<str:title>/", views.entry, name="entry"),
    path("search/",views.search, name="search"),
    path("edit/",views.edit, name="edit" ),
    path("save_edit/", views.save_edit,name="save_edit"),
    path("rand/",views.rand, name="rand")
]
