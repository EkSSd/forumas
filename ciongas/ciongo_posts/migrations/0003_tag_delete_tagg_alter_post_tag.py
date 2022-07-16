# Generated by Django 4.0.5 on 2022-07-15 09:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ciongo_posts', '0002_rename_puslapis_post'),
    ]

    operations = [
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, unique=True, verbose_name='tagg')),
            ],
        ),
        migrations.DeleteModel(
            name='Tagg',
        ),
        migrations.AlterField(
            model_name='post',
            name='tag',
            field=models.ManyToManyField(related_name='posts', to='ciongo_posts.tag'),
        ),
    ]