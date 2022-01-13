from django.db import models

class Tests(models.Model):
    CHOICES_2 = [
        ['OSON','OSON'],
        ['O`RTA','O`RTA'],
        ['QIYIN','QIYIN'],
    ]
    CHOICES = [
        ['a','a'],
        ['b','b'],
        ['c','c'],
        ['d','d']
    ]
    id = models.AutoField(primary_key=True,unique=True)
    level = models.CharField(choices=CHOICES_2,max_length=150, verbose_name='Qiyinlik darajasi', default='OSON')
    test =  models.TextField(verbose_name='Savol')
    a = models.CharField(max_length=450, verbose_name='A')
    b = models.CharField(max_length=450, verbose_name='B')
    c = models.CharField(max_length=450, verbose_name='C')
    d = models.CharField(max_length=450, verbose_name='D')
    right = models.CharField(choices=CHOICES,max_length=50, verbose_name='To`gri javob')
    def __str__(self):
        return f'{self.id}-{self.test}'
class Test_name(models.Model):
    name = models.CharField(max_length=150)
    id = models.AutoField(primary_key=True,unique=True)
    tests = models.ManyToManyField(Tests,verbose_name='Testlar')
    def __str__(self):
        return self.name