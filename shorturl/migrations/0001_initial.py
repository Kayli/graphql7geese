# Generated by Django 2.2.5 on 2019-09-21 21:02

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='UrlEntry',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('short_id', models.CharField(max_length=50)),
                ('value', models.CharField(max_length=2048)),
                ('created_on', models.DateTimeField(verbose_name='date added')),
            ],
        ),
    ]