from django.db import models
from django.core.validators import EmailValidator, RegexValidator


class OrderForm(models.Model):
    user_name = models.CharField('User', max_length=50)
    user_email = models.EmailField('E-mail', validators=[EmailValidator],
                                   max_length=100, null=True, blank=True, unique=True)
    phone_regex = RegexValidator(regex=r'^\+?1?\d{9,12}$',
                                 message="Phone number format: '+999999999'. Up to 12 digits allowed.")
    user_phone = models.CharField('Phone', validators=[phone_regex], max_length=12, blank=True, unique=True)
    text = models.TextField('Text', null=True, blank=True)
    order_date = models.DateTimeField('Register date', auto_now_add=True)

    def __str__(self):
        return self.user_name
