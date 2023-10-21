# Generated by Django 4.2.6 on 2023-10-20 16:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0002_alter_category_options_remove_product_image_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='card_type',
            field=models.CharField(choices=[('horizontal', 'Horizontal Card'), ('vertical', 'Vertical Card')], default='vertical', max_length=10),
        ),
    ]