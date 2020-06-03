# Generated by Django 2.1.1 on 2020-06-03 05:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('realstateapp', '0005_delete_cartdata'),
    ]

    operations = [
        migrations.CreateModel(
            name='CartData',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Cart_ID', models.CharField(max_length=100)),
                ('Order_ID', models.CharField(max_length=50)),
                ('Email', models.CharField(max_length=100)),
                ('Buyer_ID', models.CharField(max_length=100)),
            ],
            options={
                'db_table': 'CartData',
            },
        ),
    ]
