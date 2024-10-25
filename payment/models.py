from django.db import models
import uuid

# Create your models here.
class Payment(models.Model):
    # personal details 
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    phone = models.CharField(max_length=255)
    email = models.EmailField()
    order_notes = models.TextField()

    # delivery Address
    delivery_address = models.CharField(max_length=1000)
    additional_info = models.TextField()

    # cart and payment
    amount = models.PositiveIntegerField()
    ref = models.UUIDField(default=uuid.uuid4,editable=False,unique=True)
   
    verified = models.BooleanField(default=False)
    date_created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ('-date_created',)

    def __str__(self) -> str:
        return f'Payment: {self.amount}'

    
    @property
    def amount_value(self) -> int:
        self.amount * 100
        return self.amount*100