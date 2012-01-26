from django.db import models
import uuid


# Create your models here.
class CubeItem(models.Model):
    cubeValue = models.CharField(max_length=100, unique=True)

    parentKey = models.CharField(max_length=100)
    cubeType = models.CharField(max_length=100)

    class Meta:
        verbose_name = ('CubeItem')
        verbose_name_plural = ('CubeItems')

    def make_uuid():
        return str(uuid.uuid4())

    keyName = models.CharField(max_length=36, primary_key=True,
      default=make_uuid, editable=False)

    def __unicode__(self):
        return unicode(self.cubeValue)
