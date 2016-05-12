"""Views for albums and photos."""
from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from imager_images.forms import NewAlbumForm, NewPhotoForm
from imager_images.models import Album, Photo
from django.views.generic.edit import UpdateView, CreateView
from django.forms import ChoiceField
import datetime
from django.shortcuts import redirect


@login_required(redirect_field_name='/')
def create_new_album(request):
    """Create new album."""
    user = User.objects.get(pk=request.user.id)
    if request.method == 'POST':
        form = NewAlbumForm(request.POST)
        album = Album(title=form.data['title'], description=form.data['description'])
        album.save()
        user.albums.add(album)
        return redirect('/images/library/')
    elif request.method == 'GET':
        new_album_form = NewAlbumForm()
        return render(request, 'newalbum.html', context={
            'new_album_form': new_album_form
    })


@login_required(redirect_field_name='/')
def upload_new_photo(request):
    """Upload new photo."""
    user = User.objects.get(pk=request.user.id)
    if request.method == 'POST':
        form = NewPhotoForm(request.POST, request.FILES)
        new_photo = Photo(title=form.data['title'], description=form.data['description'], img_file=request.FILES['img_file'])
        new_photo.owner = user
        new_photo.save()
        return redirect('/images/library/')
    elif request.method == 'GET':
        new_photo_form = NewPhotoForm()
        return render(request, 'newphoto.html', context={
            'new_photo_form': new_photo_form
    })


class Edit_Photo(UpdateView):
    """A form to edit photos."""

    model = Photo
    template_name = 'photo_update_form.html'
    fields = ['title', 'description', 'in_album']
    success_url = '/images/library/'

    def form_valid(self, form):
        """Validate form."""
        form.instance.date_modified = datetime.datetime.now()
        return super(Edit_Photo, self).form_valid(form)




class Edit_Album(UpdateView):
    """A form to edit photos."""

    model = Album
    fields = ['title', 'description', 'published', 'cover']
    template_name = 'album_update_form.html'
    success_url = '/images/library/'

    def form_valid(self, form):
        """Validate form."""
        form.instance.date_modified = datetime.datetime.now()
        return super(Edit_Album, self).form_valid(form)
