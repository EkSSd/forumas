# Generated by Django 4.0.5 on 2022-07-15 11:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ciongo_posts', '0005_post_post_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='post_image',
            field=models.ImageField(blank=True, null=True, upload_to='uploads'),
        ),
    ]