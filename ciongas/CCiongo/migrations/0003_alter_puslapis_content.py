# Generated by Django 4.0.5 on 2022-07-14 09:35

import ckeditor_uploader.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('CCiongo', '0002_alter_puslapis_content'),
    ]

    operations = [
        migrations.AlterField(
            model_name='puslapis',
            name='content',
            field=ckeditor_uploader.fields.RichTextUploadingField(blank=True, max_length=20000, null=True),
        ),
    ]