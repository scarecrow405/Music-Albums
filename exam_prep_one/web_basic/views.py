from django import forms
from django.shortcuts import render, redirect

from exam_prep_one.web_basic.forms import ProfileForm, AlbumForm
from exam_prep_one.web_basic.models import Profile, Album


# CUSTOM FUNCTIONS
def get_profile():
    return Profile.objects.first()


# HOME PAGE -----------
def home_page(request):
    profile = get_profile()
    albums = Album.objects.order_by('pk').all()

    if request.method == "POST":
        form = ProfileForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home_page')
    form = ProfileForm()

    context = {
        "profile": profile,
        "form": form,
        "albums": albums
    }

    template = "home/home-no-profile.html" if profile is None else "home/home-with-profile.html"

    return render(
        request, template, context)


# ALBUMS -----------
def album_add(request):
    profile = get_profile()

    if request.method == "POST":
        form = AlbumForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('home_page')
    form = AlbumForm()

    context = {
        "form": form,
        "profile": profile
    }

    return render(
        request, "albums/add-album.html", context)


def album_details(request, pk):
    profile = get_profile()
    album = Album.objects \
        .filter(pk=pk) \
        .get()

    context = {
        "album": album,
        "profile": profile
    }

    return render(
        request, "albums/album-details.html", context)


def album_edit(request, pk):
    profile = get_profile()
    album = Album.objects \
        .filter(pk=pk) \
        .get()

    album_form = AlbumForm(instance=album)

    if request.method == "POST":
        album_form = AlbumForm(request.POST, instance=album)

        if album_form.is_valid():
            album_form.save()
            return redirect('home_page')

    context = {
        "album_form": album_form,
        "album": album,
        "profile": profile
    }

    return render(
        request, "albums/edit-album.html", context)


def album_delete(request, pk):
    profile = get_profile()
    album = Album.objects \
        .filter(pk=pk) \
        .get()

    album_form = AlbumForm(instance=album)
    for field in album_form.fields.values():
        field.widget.attrs['disabled'] = True

    if request.method == "POST":
        album.delete()
        return redirect('home_page')

    context = {
        "album_form": album_form,
        "album": album,
        "profile": profile
    }

    return render(
        request, "albums/delete-album.html", context)


# PROFILE -----------
def profile_details(request):
    profile = get_profile()
    albums_len = Album.objects.count()

    context = {
        "profile": profile,
        "albums_len": albums_len
    }

    return render(
        request, "profiles/profile-details.html", context)


def profile_edit(request):
    profile = get_profile()
    profile_form = ProfileForm(instance=profile)

    if request.method == "POST":
        profile_form = ProfileForm(request.POST, instance=profile)

        if profile_form.is_valid():
            profile_form.save()
            return redirect('profile_details')

    context = {
        "profile": profile,
        "profile_form": profile_form
    }

    return render(request, "profiles/profile-edit.html", context)


def profile_delete(request):
    profile = get_profile()
    profile_form = ProfileForm(instance=profile)

    for _, field in profile_form.fields.items():
        field.widget = forms.HiddenInput()

    if request.method == "POST":
        profile.delete()
        Album.objects.all().delete()
        return redirect('home_page')

    context = {
        "profile_form": profile_form,
        "profile": profile
    }

    return render(
        request, "profiles/profile-delete.html", context)
