# Generated by Django 2.1.1 on 2018-09-26 21:01

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='CollectionCentre',
            fields=[
                ('id', models.AutoField(help_text='Unique ID of the collection centre', primary_key=True, serialize=False)),
                ('lat', models.CharField(help_text='Latitude', max_length=20)),
                ('lng', models.CharField(help_text='Longitude', max_length=20)),
                ('location', models.CharField(help_text='Location name', max_length=200)),
                ('user', models.ForeignKey(db_column='user', on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
