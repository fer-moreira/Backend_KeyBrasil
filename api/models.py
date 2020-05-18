from django.db import models
from django.conf import settings
from datetime import datetime, timezone, timedelta
from django.utils.safestring import mark_safe
from django.contrib.auth.models import User
from django.db.models import Sum


class BrandsModel (models.Model):
    id         = models.AutoField(primary_key=True)
    slug       = models.SlugField(max_length=150)
    name       = models.CharField(verbose_name="Name", max_length=150)
    text       = models.TextField(verbose_name="Description", max_length=500)
    image      = models.CharField(verbose_name="Image", max_length=450)
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Updated at')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Created at')

    def preview(self):
        return mark_safe("""
        <img src="{0}" style="
            max-width:150px; 
            max-height:150px;
            width:auto;
            height:auto;
        "/>
        """.format(self.image))

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = 'Brand'
        verbose_name_plural = 'Brands'

class ProductImageModel (models.Model):
    id          = models.AutoField(primary_key=True)
    name        = models.CharField(verbose_name="Name", max_length=500)
    url         = models.CharField(verbose_name="Url",max_length=500)
    updated_at  = models.DateTimeField(auto_now=True, verbose_name='Updated at')
    created_at  = models.DateTimeField(auto_now_add=True, verbose_name='Created at')

    def preview(self):
        return mark_safe("""
        <img src="{0}" style="
            max-width:300px; 
            max-height:300px;
            width:auto;
            height:auto;
        "/>
        """.format(self.url))

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = 'Image'
        verbose_name_plural = 'Images'

class SwitchTypesModel (models.Model):
    id          = models.AutoField(primary_key=True)
    name        = models.CharField(verbose_name="Name",max_length=150)
    model_name  = models.CharField(verbose_name="Model",max_length=150)
    slug        = models.SlugField(max_length=150)
    images      = models.ManyToManyField(ProductImageModel)
    updated_at  = models.DateTimeField(auto_now=True, verbose_name='Updated at')
    created_at  = models.DateTimeField(auto_now_add=True, verbose_name='Created at')

    def preview(self):
        return mark_safe("""
        <img src="{0}" style="
            max-width:100px; 
            max-height:100px; 
            width:auto; 
            height:auto;
        "/>
        """.format(self.images.all()[0].url))

    def __str__(self):
        return  "{0} - {1}".format(self.id, self.name)
    
    class Meta:
        verbose_name = 'Switch'
        verbose_name_plural = 'Switches'

class ProductModel (models.Model):
    id          = models.AutoField(primary_key=True)
    name        = models.CharField(verbose_name="Product Name",max_length=150)
    model_name  = models.CharField(verbose_name="Product Model",max_length=150)
    brand_fk = models.ForeignKey(
        BrandsModel, 
        on_delete=models.CASCADE,
        verbose_name = "Brand",
        null=False,
        blank=False
    )
    slug        = models.SlugField(max_length=150)
    price       = models.FloatField(verbose_name="Price", max_length=150)
    stock_count = models.IntegerField(verbose_name="In Stock")
    switch_type = models.ManyToManyField(SwitchTypesModel)
    images      = models.ManyToManyField(ProductImageModel)
    updated_at  = models.DateTimeField(auto_now=True, verbose_name='Updated at')
    created_at  = models.DateTimeField(auto_now_add=True, verbose_name='Created at')

    @property
    def star_value (self):
        """ Return calculated STARS ratio in review  """
        reviews = ProductReviewModel.objects.filter(product_fk__id=self.id)
        max_rating = reviews.aggregate(sum_rating=Sum('review_rating')).get('sum_rating')
        rating_count = len(reviews)
        rating_ratio = (max_rating / rating_count)
        return rating_ratio

    def preview (self):
        """ Return first image from manytomany to show in admin """
        return mark_safe("""
        <img src="{0}" style="
            max-width:300px;
            max-height:300px; 
            width:auto; 
            height:auto;"
        />
        """.format(self.images.all()[0].url))


    def __str__(self):
        return str("{0} {1}").format(self.brand_fk.name, self.name)
    
    class Meta:
        verbose_name = 'Keyboard'
        verbose_name_plural = 'Keyboards'

class ProductReviewModel (models.Model):
    product_fk = models.ForeignKey(
        ProductModel, 
        on_delete=models.CASCADE, 
        null=False,
        blank=False
    )

    id            = models.AutoField(primary_key=True)
    author_name   = models.CharField(verbose_name="Author Name",max_length=450)
    author_email  = models.CharField(verbose_name="Author Email",max_length=450)
    review_text   = models.CharField(verbose_name="Description", max_length=450)
    review_rating = models.IntegerField(verbose_name="Rating")
    updated_at    = models.DateTimeField(auto_now=True, verbose_name='Updated at')
    created_at    = models.DateTimeField(auto_now_add=True, verbose_name='Created at')

    def __str__(self):
        return str(self.author_name + " | " + str(self.review_text[:20]).rstrip())
    
    class Meta:
        verbose_name = 'Review'
        verbose_name_plural = 'Reviews'

class SlidshowProductsModel (models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(verbose_name="Slideshow Name",max_length=200)
    products = models.ManyToManyField(ProductModel, verbose_name="Products")
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Updated at')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Created at')

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = "Slideshow"
        verbose_name_plural = 'Slideshow'
