# Generated by Django 4.2.6 on 2023-12-12 15:50

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('wishlist', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='wishlist',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, default=datetime.datetime(2023, 12, 12, 15, 50, 7, 902732, tzinfo=datetime.timezone.utc)),
            preserve_default=False,
        ),
    ]
