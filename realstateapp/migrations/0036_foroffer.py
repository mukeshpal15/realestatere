# Generated by Django 2.1.1 on 2020-07-06 06:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('realstateapp', '0035_auto_20200702_1715'),
    ]

    operations = [
        migrations.CreateModel(
            name='foroffer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='offerimage/')),
                ('Email_ID', models.CharField(default='', max_length=100)),
            ],
            options={
                'db_table': 'foroffer`',
            },
        ),
    ]