from django import forms


class walluploadform(forms.Form):
    image=forms.FileField()
    imagename=forms.CharField(max_length=300)
    category=forms.CharField(max_length=100)


class uregform(forms.Form):
    fullname=forms.CharField(max_length=30)
    username=forms.CharField(max_length=30)
    email=forms.EmailField()
    password=forms.CharField(max_length=30)

class uloginform(forms.Form):
    username=forms.CharField(max_length=30)
    password=forms.CharField(max_length=30)
