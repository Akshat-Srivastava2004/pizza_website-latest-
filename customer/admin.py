from django.contrib import admin
from .models import Feedback, CardInfo,PizzaInfo,Ordersummary

admin.site.site_header = "TOPTOPPING PIZZA"

@admin.register(CardInfo)
class PaymentAdmin(admin.ModelAdmin):
    list_display = ("cardholder_name", "card_number", "expiry_date", "cvv")

@admin.register(Feedback)
class FeedbackAdmin(admin.ModelAdmin):
    list_display = ("customer_name", "customer_email", "title", "message")


@admin.register(PizzaInfo)
class PizzaInfoAdmin(admin.ModelAdmin):
    list_display = ("name", "size", "price", "description")


@admin.register(Ordersummary)
class OrdersummaryAdmin(admin.ModelAdmin):
    list_display = ("name", "size", "price", "description")
