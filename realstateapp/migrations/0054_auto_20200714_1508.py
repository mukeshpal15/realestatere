# Generated by Django 2.1.1 on 2020-07-14 09:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('realstateapp', '0053_loandetails'),
    ]

    operations = [
        migrations.AlterField(
            model_name='loandetails',
            name='date',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
