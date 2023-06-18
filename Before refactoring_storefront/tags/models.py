from django.db import models
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes.fields import GenericForeignKey

# Create your models here.
class Tag(models.Model):
    label = models.CharField(max_length=255)

class TaggedItem(models.Model):
    # What tag applied to what object
    tag = models.ForeignKey(Tag, on_delete=models.CASCADE)
    #Type (product or video or article)
    #Id
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    # if ID is not integer and ID is GUID, PositiveIntegerField will not work
    object_id = models.PositiveIntegerField()
    # we can read the actual object, that the particuler tag is applied to
    content_object = GenericForeignKey()

