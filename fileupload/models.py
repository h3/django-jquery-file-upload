from django.db import models
from django.contrib.auth.models import User
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes import generic

from fileupload.conf import settings


class BaseFileUpload(models.Model):
    user = models.ForeignKey(User, blank=True, null=True)
    content_type = models.ForeignKey(ContentType)
    object_id = models.PositiveIntegerField()
    content_object = generic.GenericForeignKey('content_type', 'object_id')
    date_created = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)

    def __unicode__(self):
        return u'%s' % self.document

    class Meta:
        abstract = True


class FileUpload(BaseFileUpload):
    document = models.FileField(upload_to=settings.UPLOAD_FILES_TO)


class ImageUpload(BaseFileUpload):
    document = models.FileField(upload_to=settings.UPLOAD_IMAGES_TO)


#class Picture(models.Model):
#
#    slug = models.SlugField(max_length=50, blank=True)
#
#    def __unicode__(self):
#        return '%s' % (self.file)
#
#    @models.permalink
#    def get_absolute_url(self):
#        return ('upload-new', )
#
#    def save(self, *args, **kwargs):
#        self.slug = self.file.name
#        super(Picture, self).save(*args, **kwargs)
#
#    def delete(self, *args, **kwargs):
#        self.file.delete(False)
#        super(Picture, self).delete(*args, **kwargs)
#
#
#class PictureForm(forms.ModelForm):
#    class Meta:
#        model = Picture
#        fields = ['file', ]
#
#    def UploadImage(request):
#        """Upload Images"""
#        if request.method == 'POST':
#            form = PictureForm(request.POST, request.FILES)
#            if form.is_valid():
#                obj = form.save(commit=False)
#                obj.user = request.user
#                obj.save()
#                return HttpResponseRedirect(".")
#        else:
#            form = PictureForm()
#
#        return render(request, 'picture_form.html', {
#        'form': form,
#        })
