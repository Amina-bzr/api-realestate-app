# Generated by Django 4.1.4 on 2023-02-01 16:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('realestate', '0022_contact_picture_alter_annonce_commune_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='annonce',
            name='Commune',
            field=models.CharField(default='Alger', max_length=25),
        ),
        migrations.AlterField(
            model_name='annonce',
            name='Wilaya',
            field=models.CharField(default='Alger', max_length=25),
        ),
    ]
