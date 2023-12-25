# Generated by Django 4.2.6 on 2023-12-20 20:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0013_alter_product_rating_alter_review_user_rating'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='rating',
        ),
        migrations.AlterField(
            model_name='review',
            name='user_rating',
            field=models.FloatField(default=0.0),
        ),
    ]