# Generated by Django 2.1.1 on 2020-07-14 09:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('realstateapp', '0051_remove_loandetails_date'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Loandetails',
        ),
    ]