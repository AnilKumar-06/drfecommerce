from django.contrib import admin
from .models import Brand, Product, Category, ProductLine
# Register your models here.


class ProductInlineAdmin(admin.TabularInline):
    model = ProductLine

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    inlines = [
        ProductInlineAdmin
    ]

admin.site.register(Brand)
admin.site.register(Category)
