from django.db import models

# Create your models here.

class CustomerDb(models.Model):
    customer_name=models.CharField(max_length=100)
    phone=models.CharField(max_length=15,unique=True)
    email=models.EmailField()
    place=models.CharField(max_length=100)

    def __str__(self):
        return self.customer_name

class RepairDb(models.Model):
    STATUS_CHOICES=[
        ("Pending","Pending"),
        ("In Progress","In Progress"),
        ("Completed","Completed"),
        ("Delivered","Delivered"),
    ]
    customer=models.ForeignKey(CustomerDb,on_delete=models.CASCADE,related_name='repairs')
    device_name = models.CharField(max_length=100)
    problem_description = models.TextField()
    repair_status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default='Pending'
    )
    repair_charge = models.DecimalField(
        max_digits=8,
        decimal_places=2,
        null=True,
        blank=True
    )
    received_date = models.DateField(auto_now_add=True)

