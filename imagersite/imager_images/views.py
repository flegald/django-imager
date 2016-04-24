"""Views for albums and photos."""
from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from forms import NewAlbumForm, NewPhotoForm
from models import Album, Photo
from django.views.generic.edit import UpdateView, CreateView
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


class Upload_Photo(CreateView):
    """Form to upload photos."""

    model = Photo
    fields = ['title', 'description', 'img_file', 'published', 'in_album']
    template_name = 'newphoto.html'
    success_url = '/images/library'

    def form_valid(self, form):
        """Validate form."""
        form.instance.date_uploaded = datetime.datetime.now()
        return super(Upload_Photo, self).form_valid(form)


class Edit_Photo(UpdateView):
    """A form to edit photos."""

    model = Photo
    fields = ['title', 'description', 'published', 'in_album']
    template_name = 'photo_update_form.html'
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
        return super(Edit_Ablum, self).form_valid(form)
