# Generated by Django 3.2.4 on 2021-07-14 05:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('items', '0008_auto_20210714_0151'),
    ]

    operations = [
        migrations.RenameField(
            model_name='orderitem',
            old_name='itme',
            new_name='item',
        ),
    ]
