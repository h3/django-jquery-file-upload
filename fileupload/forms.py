from django import forms
from django.shortcuts import render
from django.http import HttpResponseRedirect

from fileupload.models import FileUpload, ImageUpload


class FileUploadForm(forms.ModelForm):
    class Meta:
        model = FileUpload
        fields = ['document', ]

    def UploadImage(request):
        """Upload Images"""
        if request.method == 'POST':
            form = FileUploadForm(request.POST, request.FILES)
            if form.is_valid():
                obj = form.save(commit=False)
                obj.user = request.user
                obj.save()
                return HttpResponseRedirect(".")
        else:
            form = FileUploadForm()

        return render(request, 'picture_form.html', {
            'form': form,
        })

class ImageUploadForm(FileUploadForm):
    class Meta:
        model = ImageUpload
        fields = ['document', ]
