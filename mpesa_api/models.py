from django.db import models


# Create your models here.


class BaseModel(models.Model):
    """
    BaseModel class that defines the common fields for all the models
    """

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


# M-pesa Payment models


class MpesaCalls(BaseModel):
    """
    MpesaCalls class that defines the fields for the MpesaCalls model
    """

    ip_address = models.TextField()
    caller = models.TextField()
    conversation_id = models.TextField()
    content = models.TextField()

    class Meta:
        db_table = "mpesa_calls"
        verbose_name = "Mpesa Call"
        verbose_name_plural = "Mpesa Calls"


class MpesaCallbacks(BaseModel):
    """
    MpesaCallbacks class that defines the fields for the MpesaCallbacks model
    """

    ip_address = models.TextField()
    caller = models.TextField()
    conversation_id = models.TextField()
    content = models.TextField()

    class Meta:
        db_table = "mpesa_callbacks"
        verbose_name = "Mpesa Callback"
        verbose_name_plural = "Mpesa Callbacks"


class MpesaPayments(BaseModel):
    """
    Mpesa Payments class that defines the fields for the MpesaPayments model
    """

    amount = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField()
    type = models.TextField()
    reference = models.TextField()
    first_name = models.CharField(max_length=100)
    middle_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    phone_number = models.TextField()
    organization_balance = models.DecimalField(max_digits=10, decimal_places=2)

    class Meta:
        verbose_name = "Mpesa Payment"
        verbose_name_plural = "Mpesa Payments"

    def __str__(self):
        return self.first_name
