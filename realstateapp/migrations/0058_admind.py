# Generated by Django 2.1.1 on 2020-07-14 10:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('realstateapp', '0057_loandetails'),
    ]

    operations = [
        migrations.CreateModel(
            name='admind',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.CharField(max_length=100)),
                ('password', models.CharField(max_length=100)),
            ],
        ),
    ]
