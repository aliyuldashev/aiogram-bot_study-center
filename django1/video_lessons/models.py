from django.db import models

# Create your models here.
class BigFieald(models.Model):
    id = models.AutoField(primary_key=True,unique = True)
    name = models.CharField(max_length=150, null=True, blank=True)
    def __str__(self):
        return self.name
class SecandField(models.Model):
    id = models.AutoField(primary_key=True,unique=True)
    name = models.CharField(max_length=150, null=True, blank=True)
    bigfield = models.ForeignKey(BigFieald,null=False, on_delete=models.CASCADE, verbose_name='BIRINCHI KATEGORIYA')

class VideoLessans(models.Model):
    id = models.AutoField(primary_key=True,unique=True)
    Video = models.FileField(upload_to='images',verbose_name='VIDEO')
    secondfield = models.ForeignKey(SecandField,null=False, on_delete=models.CASCADE,verbose_name='IKKINCHI KATEGORIYA')
    character = models.TextField(null=False)
    name = models.CharField(max_length=50,verbose_name='nechinchi dars')


