from django.db import models

# model
class Product(models.Model):
    code = models.CharField(max_length=20)
    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.IntegerField()
    sizes = (
        ('S', 'Small'),
        ('M', 'Medium'),
        ('L', 'Large'),
        ('F', 'Free'),
    )
    size = models.CharField(choices=sizes, max_length=1)

    def __str__(self):
        return self.code
    
    def save(self, *args, **kwargs):
        # 생성될 때 stock quantity를 0으로 초기화
        if not self.pk:
            self.stock_quantity = 0
        super().save(*args, **kwargs)
