# Generated by Django 4.1.4 on 2023-01-12 19:26

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('realestate', '0009_alter_annonce_annonceur'),
    ]

    operations = [
        migrations.AlterField(
            model_name='annonce',
            name='annonceur',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
