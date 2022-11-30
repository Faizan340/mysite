from django.contrib import admin
from post.models import Postmodel,Commentmodel

class PostAdmin(admin.ModelAdmin):
    readonly_fields = ("created_on", "updated_on")
# Register your models here.
admin.site.register(Postmodel,PostAdmin)
admin.site.register(Commentmodel)