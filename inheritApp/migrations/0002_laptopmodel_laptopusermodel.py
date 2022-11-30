# Generated by Django 4.1.3 on 2022-11-30 06:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('inheritApp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='LaptopModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('laptop_name', models.CharField(blank=True, max_length=100, null=True)),
                ('price', models.IntegerField(blank=True, null=True)),
                ('slug', models.SlugField(unique=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='LaptopUserModel',
            fields=[
                ('laptopmodel_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='inheritApp.laptopmodel')),
                ('name', models.CharField(blank=True, max_length=100, null=True)),
                ('age', models.IntegerField(blank=True, null=True)),
            ],
            bases=('inheritApp.laptopmodel',),
        ),
    ]
