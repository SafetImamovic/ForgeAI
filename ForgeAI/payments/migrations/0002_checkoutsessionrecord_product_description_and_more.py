# Generated by Django 5.0.6 on 2024-06-01 19:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('payments', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='checkoutsessionrecord',
            name='product_description',
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name='checkoutsessionrecord',
            name='product_name',
            field=models.CharField(blank=True, max_length=255),
        ),
    ]
