# Generated by Django 5.0.6 on 2024-09-06 09:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('carts', '0002_wishlist_wishlist_items'),
    ]

    operations = [
        migrations.DeleteModel(
            name='wishlist',
        ),
        migrations.DeleteModel(
            name='wishlist_items',
        ),
    ]