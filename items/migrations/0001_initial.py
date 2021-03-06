# Generated by Django 3.2.4 on 2021-06-10 00:40

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('barCode', models.IntegerField(max_length=10)),
                ('name', models.CharField(max_length=25)),
                ('supplier', models.CharField(max_length=30)),
                ('quantity', models.IntegerField(max_length=10)),
                ('price', models.DecimalField(decimal_places=2, max_digits=6)),
                ('dateAdded', models.DateTimeField()),
            ],
        ),
        migrations.CreateModel(
            name='Recipt',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('items', models.ManyToManyField(to='items.Item')),
            ],
        ),
    ]
