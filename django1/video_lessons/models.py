from django.db import models

# Create your models here.
class FirstField(models.Model):
    id = models.AutoField(primary_key=True,unique = True)
    name = models.CharField(max_length=150, null=True, blank=True)
    def __str__(self):
        return self.name
class SecandField(models.Model):
    id = models.AutoField(primary_key=True,unique=True)
    name = models.CharField(max_length=150, null=True, blank=True)
    bigfield = models.ForeignKey(FirstField,null=False, on_delete=models.CASCADE, verbose_name='BIRINCHI KATEGORIYA')
    def __str__(self):
        return self.name
class LastField(models.Model):
    id = models.AutoField(primary_key=True,unique=True)
    firstfield = models.ForeignKey(FirstField,null=False, on_delete=models.CASCADE,verbose_name='BIRINCHI KATEGORIYA')
    secondfield = models.ForeignKey(SecandField,blank=True,null=True,default=None, on_delete=models.CASCADE,verbose_name='IKKINCHI KATEGORIYA')
    dates = models.ManyToManyField('Post',related_name='malumot',verbose_name='Malumotlar')
    name = models.CharField(max_length=50,verbose_name='NOMI')
    def __str__(self):
        return self.name
class Post(models.Model):
    CHOICES = [
        ['video','video'],
        ['post','post'],
        ['photo','photo'],
        ['pdf','pdf']
    ]
    id = models.AutoField(primary_key=True,unique=True)
    type = models.CharField(choices=CHOICES,max_length=150,verbose_name='TURI')
    File = models.FileField(upload_to='images',verbose_name='FILE',blank=True)
    text = models.TextField(verbose_name='FILE TEKSTI')
    def __str__(self):
        return self.text


