# Generated by Django 4.1.7 on 2023-04-03 13:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0006_project_hidden'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='title_long',
            field=models.CharField(blank=True, max_length=1000),
        ),
        migrations.AlterField(
            model_name='project',
            name='description',
            field=models.TextField(),
        ),
    ]
