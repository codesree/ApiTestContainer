# Generated by Django 2.0.7 on 2018-12-20 19:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('testapi', '0002_userpro'),
    ]

    operations = [
        migrations.DeleteModel(
            name='tag_check',
        ),
        migrations.RemoveField(
            model_name='userpro',
            name='user',
        ),
        migrations.DeleteModel(
            name='Userpro',
        ),
    ]
