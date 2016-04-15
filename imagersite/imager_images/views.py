# """For create new album only(no img upload)."""
# from django.shortcuts import render
# from django import forms
# from .models import PUB_CHOICE


# class NewAlbumForm(forms.Form):
#     title = forms.CharField(label='Title', initial='untitled')
#     description = forms.CharField(widget=forms.Textarea(), label='Description')
#     privacy = forms.ChoiceField(widget=forms.RadioSelect(),
#                                 label='Privacy',
#                                 choices=PUB_CHOICE,
#                                 default='Public')

# def create_new_album(request):
#     new_album_form = NewAlbumForm()
#     return render(request, 'newalbum.html', context={
#         'new_album_form': new_album_form
#     })
