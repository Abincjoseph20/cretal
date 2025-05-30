from django.db import models

# Create your models here.


CATEGORY_CHOICE=(
    ('CS','Casual shoe Men'),
    ('CW','Casual Shoe Women'),
    ('BT','Boots'),
    ('SS','Sports Shoe'),
    ('KD','Kids'),
    ('JC','Jersey'),
    ('TS','T-Shirts'),
    ('PN','Pants'),
)


class Product(models.Model):
    title=models.CharField(max_length=150)
    selling_price=models.FloatField()
    discounted_price = models.FloatField()
    description = models.TextField()
    category = models.CharField(choices=CATEGORY_CHOICE,max_length=2)
    product_image = models.ImageField(upload_to='product')
    product_quantity = models.FloatField()
    modified_date = models.DateField(auto_now=True)
    created_date = models.DateField(auto_now_add=True)
    def __str__(self):
        return self.title