# Generated by Django 4.2.6 on 2023-12-09 12:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0007_review_rate'),
    ]

    operations = [
        migrations.RenameField(
            model_name='review',
            old_name='rate',
            new_name='rating',
        ),
    ]
