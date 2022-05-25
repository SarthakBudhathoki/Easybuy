from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=200, db_index=True)
    slug = models.SlugField(max_length=200, unique=True)
    class Meta:
        ordering = ('name',)
        verbose_name = 'category'
        verbose_name_plural = 'categories'
    def __str__(self):
        return self.name

    
class Product(models.Model):
    id=models.AutoField(auto_created=True,primary_key=True)
    category = models.ForeignKey(Category, related_name='products', on_delete=models.CASCADE)
    name = models.CharField(max_length=200, db_index=True)
    slug = models.SlugField(max_length=200, db_index=True)
    image=models.ImageField(upload_to="media/productimage/")
    description = models.TextField(blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    available = models.BooleanField(default=True)
   
    
    class Meta:
        ordering = ('name',)
        index_together = (('id', 'slug'),)
    def __str__(self):
        return self.name

class Blogs(models.Model):
    blog_id=models.AutoField(auto_created=True,primary_key=True)
    blog_name=models.CharField(max_length=200)
    blog_details=models.CharField(max_length=200)
    blog_image=models.FileField(upload_to='blog_image')

    class Meta:
        db_table="blog"


# RATE_CHOICES = [
#     (1,'1 - very bad'),
#     (2,'2 - bad'),
#     (3,'3 - decent'),
#     (4,'4 - good'),
#     (5,'5 - perfect'),
# ]

# class review(models.model){
#     rate = models.PositiveSmallIntergerField()
# }