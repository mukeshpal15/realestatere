from django import forms

class ImageUploadForm(forms.Form):
	image = forms.ImageField()
	
class upload_image(forms.Form):
	img=forms.ImageField()