from django.db import models

# Create your models here.
class CubeItem(models.Model):
    cubeValue = models.CharField(max_length=100)
    keyName = models.CharField(max_length=100)
    parentKey = models.CharField(max_length=100)
    cubeType = models.CharField(max_length=100)

    class Meta:
        verbose_name = ('CubeItem')
        verbose_name_plural = ('CubeItems')

    def __unicode__(self):
        return __unicode__(self.cubeValue)
