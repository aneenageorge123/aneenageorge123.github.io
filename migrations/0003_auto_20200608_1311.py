# Generated by Django 2.2.6 on 2020-06-08 07:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stockm', '0002_admindb_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='admindb',
            name='image',
            field=models.ImageField(default='', upload_to='image/'),
        ),
    ]
