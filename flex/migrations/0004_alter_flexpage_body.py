# Generated by Django 5.1.4 on 2025-01-09 01:27

import wagtail.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('flex', '0003_alter_flexpage_body'),
    ]

    operations = [
        migrations.AlterField(
            model_name='flexpage',
            name='body',
            field=wagtail.fields.StreamField([('title_and_text', 2), ('full_richtext', 3), ('cards', 11)], blank=True, block_lookup={0: ('wagtail.blocks.CharBlock', (), {'help_text': 'Add your title', 'required': True}), 1: ('wagtail.blocks.TextBlock', (), {'help_text': 'Add additional text', 'required': True}), 2: ('wagtail.blocks.StructBlock', [[('title', 0), ('text', 1)]], {}), 3: ('streams.blocks.RichTextBlock', (), {}), 4: ('wagtail.images.blocks.ImageChooserBlock', (), {'required': True}), 5: ('wagtail.blocks.CharBlock', (), {'max_length': 40, 'required': True}), 6: ('wagtail.blocks.TextBlock', (), {'max_length': 200, 'required': True}), 7: ('wagtail.blocks.PageChooserBlock', (), {'required': False}), 8: ('wagtail.blocks.URLBlock', (), {'required': False}), 9: ('wagtail.blocks.StructBlock', [[('image', 4), ('title', 5), ('text', 6), ('button_page', 7), ('button_url', 8)]], {}), 10: ('wagtail.blocks.ListBlock', (9,), {}), 11: ('wagtail.blocks.StructBlock', [[('title', 0), ('cards', 10)]], {})}, null=True),
        ),
    ]
