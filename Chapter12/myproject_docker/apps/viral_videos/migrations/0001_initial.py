# Generated by Django 2.1.2 on 2018-10-07 05:32

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ViralVideo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='creation date and time')),
                ('updated', models.DateTimeField(auto_now=True, verbose_name='modification date and time')),
                ('title', models.CharField(blank=True, max_length=200, verbose_name='Title')),
                ('embed_code', models.TextField(blank=True, verbose_name='YouTube embed code')),
                ('anonymous_views', models.PositiveIntegerField(default=0, verbose_name='Anonymous impressions')),
                ('authenticated_views', models.PositiveIntegerField(default=0, verbose_name='Authenticated impressions')),
            ],
            options={
                'verbose_name': 'Viral video',
                'verbose_name_plural': 'Viral videos',
            },
        ),
    ]
