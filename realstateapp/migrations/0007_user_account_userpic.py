# Generated by Django 2.1.1 on 2020-06-03 07:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('realstateapp', '0006_cartdata'),
    ]

    operations = [
        migrations.AddField(
            model_name='user_account',
            name='userpic',
            field=models.ImageField(default='card.jpg', upload_to='userpic'),
        ),
    ]
