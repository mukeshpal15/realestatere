# Generated by Django 2.1.1 on 2020-07-10 07:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('realstateapp', '0043_auto_20200706_1458'),
    ]

    operations = [
        migrations.CreateModel(
            name='documents',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Doc_ID', models.CharField(max_length=100)),
                ('title', models.CharField(max_length=100)),
                ('file', models.FileField(upload_to='documents/')),
            ],
        ),
    ]
