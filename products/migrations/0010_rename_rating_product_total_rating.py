# Generated by Django 4.2.6 on 2023-12-09 18:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0009_alter_review_rating'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product',
            old_name='rating',
            new_name='total_rating',
        ),
    ]
