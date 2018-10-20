# Generated by Django 2.1.1 on 2018-09-26 11:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('help', '0009_auto_20180926_1042'),
    ]

    operations = [
        migrations.AlterField(
            model_name='requests',
            name='lat',
            field=models.CharField(blank=True, help_text='Latitude', max_length=20),
        ),
        migrations.AlterField(
            model_name='requests',
            name='lng',
            field=models.CharField(blank=True, help_text='Longitude', max_length=20),
        ),
        migrations.AlterField(
            model_name='requests',
            name='phone',
            field=models.CharField(help_text='Phone of requestee', max_length=20),
        ),
        migrations.AlterField(
            model_name='requests',
            name='source',
            field=models.CharField(blank=True, help_text='Where this request call was obtained from', max_length=40),
        ),
    ]