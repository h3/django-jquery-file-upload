from django.conf import settings

UPLOAD_FILES_TO = getattr(settings, 'FILEUPLOAD_FILES_TO', 'uploads/files/')
UPLOAD_IMAGES_TO = getattr(settings, 'FILEUPLOAD_IMAGES_TO', 'uploads/images/')
