# Generated by Django 2.1.2 on 2018-10-04 06:09

from django.db import migrations, models
import music.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Track',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250, verbose_name='Name')),
                ('artist', models.CharField(max_length=250, verbose_name='Artist')),
                ('url', models.URLField(verbose_name='URL')),
                ('image', models.ImageField(blank=True, null=True, upload_to=music.models.upload_to, verbose_name='Image')),
            ],
            options={
                'verbose_name': 'Track',
                'verbose_name_plural': 'Tracks',
            },
        ),
    ]
