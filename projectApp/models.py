# productApp/models.py
from django.db import models

class Product(models.Model):
    title = models.CharField(max_length=255)
    sku = models.CharField(max_length=50)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    

class ProductImage(models.Model):
    product = models.ManyToManyField('Product', related_name='images')
    file_path = models.ImageField(upload_to='product_images/')
    thumbnail = models.ImageField(upload_to='product_images/thumbnails/')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Variant(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    


class ProductVariant(models.Model):
    variant = models.ForeignKey('Variant', on_delete=models.CASCADE)
    product = models.ForeignKey('Product', on_delete=models.CASCADE, related_name='variants')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class ProductVariantPrice(models.Model):
    product_variant_one = models.ForeignKey('ProductVariant', on_delete=models.CASCADE)
    product_variant_two = models.ForeignKey('ProductVariant', on_delete=models.CASCADE)
    product_variant_three = models.ForeignKey('ProductVariant', on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    stock = models.PositiveIntegerField()
    product = models.ForeignKey('Product', on_delete=models.CASCADE, related_name='prices')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
