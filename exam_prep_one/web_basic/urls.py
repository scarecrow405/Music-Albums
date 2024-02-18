from django.urls import path, include

from exam_prep_one.web_basic.views import home_page, \
    album_add, album_edit, album_delete, album_details, \
    profile_details, profile_delete, profile_edit

urlpatterns = [
    # HOME PAGE
    path("", home_page, name="home_page"),

    # ALBUMS
    path("album/", include([
        path("add/", album_add, name="album_add"),
        path("details/<int:pk>/", album_details, name="album_details"),
        path("edit/<int:pk>/", album_edit, name="album_edit"),
        path("delete/<int:pk>/", album_delete, name="album_delete"),
    ])),

    # PROFILE
    path("profile/", include([
        path("details/", profile_details, name="profile_details"),
        path("delete/", profile_delete, name="profile_delete"),
        path("edit/", profile_edit, name="profile_edit"),
    ])),
]
