# Generated by Django 4.1.7 on 2023-03-31 08:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0005_project_date_project_github_project_link'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='hidden',
            field=models.BooleanField(default=False),
        ),
    ]