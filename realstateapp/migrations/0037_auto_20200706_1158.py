# Generated by Django 2.1.1 on 2020-07-06 06:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('realstateapp', '0036_foroffer'),
    ]

    operations = [
        migrations.AlterField(
            model_name='foroffer',
            name='image',
            field=models.ImageField(blank=True, upload_to='offerimage/'),
        ),
    ]
