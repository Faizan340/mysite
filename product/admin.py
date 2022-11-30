from django.contrib import admin
from product.models import ProductModel,CategoryModel,OrderDetailModel

class ProductAdmin(admin.ModelAdmin):
    readonly_fields = ("created_at", "updated_at")

admin.site.register(ProductModel, ProductAdmin)
admin.site.register(CategoryModel)
admin.site.register(OrderDetailModel)