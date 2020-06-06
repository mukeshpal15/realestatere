# Generated by Django 2.1.1 on 2020-06-05 05:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('realstateapp', '0012_delete_user_account'),
    ]

    operations = [
        migrations.CreateModel(
            name='user_account',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_id', models.CharField(max_length=20)),
                ('name', models.CharField(max_length=40)),
                ('gender', models.CharField(max_length=10)),
                ('email', models.CharField(max_length=50)),
                ('address', models.CharField(max_length=400)),
                ('city', models.CharField(max_length=20)),
                ('phone', models.CharField(max_length=15)),
                ('password', models.CharField(max_length=40)),
                ('userpic', models.ImageField(blank=True, upload_to='userpic/')),
            ],
            options={
                'db_table': 'user_account',
            },
        ),
    ]