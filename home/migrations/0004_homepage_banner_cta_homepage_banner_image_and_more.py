# Generated by Django 5.1.4 on 2025-01-08 16:53

import django.db.models.deletion
import wagtail.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0003_homepage_banner_title'),
        ('wagtailimages', '0027_image_description'),
    ]

    operations = [
        migrations.AddField(
            model_name='homepage',
            name='banner_cta',
            field=models.URLField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='homepage',
            name='banner_image',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='wagtailimages.image'),
        ),
        migrations.AddField(
            model_name='homepage',
            name='banner_subtitle',
            field=wagtail.fields.RichTextField(default='this is a subtitle'),
            preserve_default=False,
        ),
    ]
