"""View handlers for imager API."""
from .permissions import IsOwner
from api.serializers import PhotoSerializer, AlbumSerializer
from imager_images.models import Photo, Album
from rest_framework.generics import ListAPIView
from rest_framework.permissions import IsAuthenticated


class PhotoListView(ListAPIView):
    """View for list view of photos."""

    queryset = Photo.objects.all()
    serializer_class = PhotoSerializer
    permission_classes = (
        IsAuthenticated,
        IsOwner,
    )

    def list(self, request, *args, **kwargs):
        """Only show logged in user's photos."""
        self.queryset = self.queryset.filter(owner=request.user)
        return super(PhotoListView, self).list(request, *args, **kwargs)


class AlbumListView(ListAPIView):
    """View for list view of albums."""

    queryset = Album.objects.all()
    serializer_class = AlbumSerializer
    permission_classes = (
        IsAuthenticated,
        IsOwner,
    )

    def list(self, request, *args, **kwargs):
        """Only show logged in user's albums."""
        self.queryset = self.queryset.filter(owner=request.user)
        return super(AlbumListView, self).list(request, *args, **kwargs)
