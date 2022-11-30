# Generated by Django 4.1.3 on 2022-11-30 09:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inheritApp', '0002_laptopmodel_laptopusermodel'),
    ]

    operations = [
        migrations.CreateModel(
            name='LocationModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('city', models.CharField(blank=True, max_length=100, null=True)),
                ('country', models.CharField(blank=True, max_length=100, null=True)),
                ('continent', models.CharField(blank=True, max_length=100, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('slug', models.SlugField(unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='LocProxyModel',
            fields=[
            ],
            options={
                'ordering': ['continent'],
                'proxy': True,
                'indexes': [],
                'constraints': [],
            },
            bases=('inheritApp.locationmodel',),
        ),
    ]