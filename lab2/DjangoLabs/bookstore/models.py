from django.db import models

# Create your models here.
class Book(models.Model):
    # slug = models.SlugField()
    name = models.CharField("Name", max_length=255, unique=True)
    description = models.TextField("Description")
    rate = models.PositiveIntegerField("priority",default=0) 
    prod_date = models.DateField(null=True)
    
    def __str__(self):
        return f"Title {self.name}"
  