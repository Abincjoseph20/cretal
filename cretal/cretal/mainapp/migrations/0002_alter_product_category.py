# Generated by Django 5.0.6 on 2024-10-01 06:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='category',
            field=models.CharField(choices=[('CS', 'Casual shoe Men'), ('CW', 'Casual Shoe Women'), ('BT', 'Boots'), ('SS', 'Sports Shoe'), ('KD', 'Kids'), ('JC', 'Jersey'), ('TS', 'T-Shirts'), ('PN', 'Pants')], max_length=2),
        ),
    ]
