# Generated by Django 5.1 on 2024-08-14 08:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('item', '0004_item_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='images/'),
        ),
    ]
