# Generated by Django 3.1.7 on 2021-04-03 17:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('BankManagement', '0003_auto_20210403_1551'),
    ]

    operations = [
        migrations.CreateModel(
            name='Currency',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('COUNTRY', models.CharField(max_length=30)),
                ('CURRENCY', models.CharField(max_length=30)),
                ('SYMBOL', models.CharField(max_length=30)),
                ('QTY', models.CharField(max_length=30)),
                ('PRICE', models.CharField(max_length=30)),
            ],
        ),
    ]
