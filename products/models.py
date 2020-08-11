from django.db import models

class Product(models.Model):
    title=models.CharField(max_length=100)
    description=models.TextField(blank=True,null=True)
    price=models.DecimalField(max_digits=10000,decimal_places=2)
    summary=models.TextField()
    featured=models.BooleanField(null=True)
    
    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse("product-detail", kwargs={"id": self.id})
    

