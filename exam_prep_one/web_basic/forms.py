from django import forms

from exam_prep_one.web_basic.models import Profile, Album


class ProfileForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.put_placeholders()

    class Meta:
        model = Profile
        fields = '__all__'

    def put_placeholders(self):
        self.fields['username'].widget.attrs['placeholder'] = 'Username'
        self.fields['email'].widget.attrs['placeholder'] = 'Email'
        self.fields['age'].widget.attrs['placeholder'] = 'Age'


class AlbumForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.put_placeholders()
        self.put_labels()

    class Meta:
        model = Album
        fields = '__all__'

    def put_placeholders(self):
        self.fields['album_name'].widget.attrs['placeholder'] = 'Album Name'
        self.fields['artist'].widget.attrs['placeholder'] = 'Artist'
        self.fields['genre'].widget.attrs['placeholder'] = 'Genre'
        self.fields['description'].widget.attrs['placeholder'] = 'Description'
        self.fields['image_url'].widget.attrs['placeholder'] = 'Image URL'
        self.fields['price'].widget.attrs['placeholder'] = 'Price'

    def put_labels(self):
        self.fields['album_name'].label = 'Album Name'
        self.fields['artist'].label = 'Artist'
        self.fields['genre'].label = 'Genre'
        self.fields['description'].label = 'Description'
        self.fields['image_url'].label = 'Image URL'
        self.fields['price'].label = 'Price'
