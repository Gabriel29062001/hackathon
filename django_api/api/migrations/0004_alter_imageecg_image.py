# Generated by Django 4.1.7 on 2023-12-03 09:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_imageecg'),
    ]

    operations = [
        migrations.AlterField(
            model_name='imageecg',
            name='image',
            field=models.ImageField(upload_to=''),
        ),
    ]