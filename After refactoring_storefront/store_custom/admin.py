from django.contrib import admin
from store.admin import ProductAdmin, ProductImageInline
from store.models import Product
from tags.models import TaggedItem
from django.contrib.contenttypes.admin import GenericTabularInline
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from .models import User

@admin.register(User)
class UserAdmin(BaseUserAdmin):
    add_fieldsets = (
        (
            None,
            {
                "classes": ("wide",),
                "fields": ("username", "password1", "password2","email", "first_name", "last_name"),
            },
        ),
    )

# Register your models here.

class TaggInline(GenericTabularInline):
    autocomplete_fields = ['tag']
    model = TaggedItem
    extra = 1

class CustomProductAdmin(ProductAdmin):
    inlines = [TaggInline, ProductImageInline]


admin.site.unregister(Product)
admin.site.register(Product, CustomProductAdmin)