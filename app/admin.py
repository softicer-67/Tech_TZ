from django.contrib import admin
from app.models import OrderForm


@admin.register(OrderForm)
class OrderFormAdmin(admin.ModelAdmin):
    list_display = ['user_name', 'user_email', 'user_phone', 'order_date']
    search_fields = ['user_name', 'user_email', 'user_phone', 'order_date']

