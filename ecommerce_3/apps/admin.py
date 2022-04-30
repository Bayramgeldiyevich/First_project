from django.contrib import admin

from .models import*


class CategoryAdmin(admin.ModelAdmin):
    list_display = ["title", "slug"]
    prepopulated_fields = {"slug":("title",)}


class ProductAdmin(admin.ModelAdmin):
    list_display = ["title", 'slug']
    prepopulated_fields = {"slug":("title",)}

admin.site.register(Category, CategoryAdmin)
admin.site.register(Customer)
admin.site.register(Product, ProductAdmin)
admin.site.register(Cart)
admin.site.register(CartProduct)
admin.site.register(Order)