# Generated by Django 4.1.7 on 2023-03-31 08:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('about', '0006_alter_bio_title'),
    ]

    operations = [
        migrations.AddField(
            model_name='photo',
            name='title',
            field=models.CharField(blank=True, max_length=200),
        ),
    ]
