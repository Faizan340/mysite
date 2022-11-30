# Generated by Django 4.1.3 on 2022-11-29 12:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sign', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='LinkModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_made_in', models.CharField(blank=True, max_length=50, null=True)),
                ('product_warranty_months', models.IntegerField(blank=True, null=True)),
                ('slug', models.SlugField(unique=True)),
            ],
        ),
    ]
