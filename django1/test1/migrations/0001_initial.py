# Generated by Django 4.0.4 on 2022-04-23 05:14

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Tests',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, unique=True)),
                ('test', models.TextField(verbose_name='Savol')),
                ('a', models.CharField(max_length=450, verbose_name='A')),
                ('b', models.CharField(max_length=450, verbose_name='B')),
                ('c', models.CharField(max_length=450, verbose_name='C')),
                ('d', models.CharField(max_length=450, verbose_name='D')),
                ('right', models.CharField(choices=[['a', 'a'], ['b', 'b'], ['c', 'c'], ['d', 'd']], max_length=50, verbose_name='To`gri javob')),
            ],
        ),
        migrations.CreateModel(
            name='Test_name',
            fields=[
                ('name', models.CharField(max_length=150)),
                ('id', models.AutoField(primary_key=True, serialize=False, unique=True)),
                ('tests', models.ManyToManyField(to='test1.tests', verbose_name='Testlar')),
            ],
        ),
    ]