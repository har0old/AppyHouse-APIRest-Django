from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator


class Company(models.Model):
    name = models.CharField(max_length=255)
    web_site = models.URLField(max_length=255)
    created = models.DateTimeField(auto_now_add=True)
    active = models.BooleanField(default=True)
    
    def __str__(self) -> str:
        return self.name
    
class Property(models.Model):
    TIPO_CHOICES = [
        ('Local', 'Local'),
        ('Apartamento', 'Apartamento'),
        ('Casa', 'Casa'),
        ('Finca', 'Finca'),
        ('Lote', 'Lote'),
        ('Otro', 'Otro'),
    ]
    LIST_GARAGE = [
        ('Si', 'Si'),
        ('No', 'No'),
    ]
    CURRENCY_CHOICES = [
        ('USD', 'Dólares estadounidenses'),
        ('EUR', 'Euros'),
        ('COP', 'Pesos colombianos'),
    ]
    
    address = models.CharField(max_length=250, default=None)
    city = models.CharField(max_length=150, default=None)
    state = models.CharField(max_length=150, default=None)
    country = models.CharField(max_length=150, default=None)
    description = models.CharField(max_length=500, default=None)
    property_Type = models.CharField(max_length=20, choices=TIPO_CHOICES, default=None)
    bedrooms = models.IntegerField(validators=[MinValueValidator(0)], default=None)
    bathrooms = models.IntegerField(validators=[MinValueValidator(0)], default=None)
    price = models.FloatField(validators=[MinValueValidator(0)], default=None)
    currency = models.CharField(max_length=3, choices=CURRENCY_CHOICES, default='USD')
    garage = models.CharField(max_length=20, choices=LIST_GARAGE, default=None)
    built_up_area_square_meters  = models.FloatField(validators=[MinValueValidator(0)], default=None)
    total_area_square_meters = models.FloatField(validators=[MinValueValidator(0)], default=None)
    image = models.CharField(max_length=900)
    active = models.BooleanField(default=True)
    company = models.ForeignKey(Company, on_delete=models.CASCADE, related_name="properties")
    created = models.DateTimeField(auto_now_add=True)
    
    def __str__(self) -> str:
        return self.address

class Comment(models.Model):
    qualification = models.PositiveIntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)])
    text = models.CharField(max_length=255, null=True)
    property = models.ForeignKey(Property, on_delete=models.CASCADE, related_name="comments")
    active = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return "Calificacion : "+str(self.qualification) +" - " +self.property.address