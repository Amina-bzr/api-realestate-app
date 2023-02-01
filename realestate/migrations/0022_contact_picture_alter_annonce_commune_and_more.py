# Generated by Django 4.1.4 on 2023-02-01 16:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('realestate', '0021_rename_addresse_annonce_addresse_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='contact',
            name='picture',
            field=models.ImageField(null=True, upload_to='userPhotos/'),
        ),
        migrations.AlterField(
            model_name='annonce',
            name='Commune',
            field=models.CharField(default='tizi', max_length=25),
        ),
        migrations.AlterField(
            model_name='annonce',
            name='Wilaya',
            field=models.CharField(default='tizi', max_length=25),
        ),
    ]
