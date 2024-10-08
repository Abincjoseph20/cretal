# Generated by Django 5.0.6 on 2024-09-02 07:47

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=150)),
                ('selling_price', models.FloatField()),
                ('discounted_price', models.FloatField()),
                ('description', models.TextField()),
                ('category', models.CharField(choices=[('CR', 'Crud'), ('MK', 'Milk'), ('LS', 'Lassi'), ('MS', 'MilkShake'), ('PN', 'Paneer'), ('GH', 'Ghee'), ('CZ', 'Cheese'), ('IH', 'Ice-cream')], max_length=2)),
                ('product_image', models.ImageField(upload_to='product')),
                ('product_quantity', models.FloatField()),
                ('modified_date', models.DateField(auto_now=True)),
                ('crated_date', models.DateField(auto_now_add=True)),
            ],
        ),
    ]
