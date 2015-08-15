from django import forms
from imgpage.models import UserObject,ImgObject

class ImgForm(forms.ModelForm):
    img_tags = forms.CharField(max_length=128,help_text="Enter Strings here:")

    class Meta:
        model = ImgObject
        fields = ('img_tags',)
