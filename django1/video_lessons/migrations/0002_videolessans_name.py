# Generated by Django 4.0 on 2022-01-02 17:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('video_lessons', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='videolessans',
            name='name',
            field=models.CharField(default='1-dars', max_length=50, verbose_name='nechinchi dars'),
            preserve_default=False,
        ),
    ]