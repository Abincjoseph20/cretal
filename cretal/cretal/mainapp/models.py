from django.db import models

# Create your models here.


CATEGORY_CHOICE=(
    ('CR','Crud'),
    ('MK','Milk'),
    ('LS','Lassi'),
    ('MS','MilkShake'),
    ('PN','Paneer'),
    ('GH','Ghee'),
    ('CZ','Cheese'),
    ('IH','Ice-cream'),
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
    crated_date = models.DateField(auto_now_add=True)
    def __str__(self):
        return self.title