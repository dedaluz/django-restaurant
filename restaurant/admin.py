from django.contrib import admin
from restaurant.models import Dish, DishCategory, DishCategoryGroup
from sorl.thumbnail.admin import AdminImageMixin
from sorl.thumbnail import get_thumbnail

class DishInlineAdmin(AdminImageMixin, admin.TabularInline):
    model = Dish
    fields = ('title', 'position', 'icon', 'status', )
    # define the sortable
    sortable_field_name = "position"
    extra = 0

class DishCategoryAdmin(admin.ModelAdmin):
    list_display = ('name', )
    prepopulated_fields = {"slug": ("name",)} 
    
    inlines = [DishInlineAdmin]

class DishAdmin(AdminImageMixin, admin.ModelAdmin):
    """docstring for DishAdmin"""
    
    prepopulated_fields = {"slug": ("title",)}   
    list_display = ('title', 'position', 'status',)
    pass
        

admin.site.register(DishCategory, DishCategoryAdmin)
admin.site.register(Dish, DishAdmin)
