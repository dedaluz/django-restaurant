from django.contrib import admin
from restaurant.models import Dish, DishCategory, DishCategoryGroup, DishPrice, DishPriceCategory
from sorl.thumbnail.admin import AdminImageMixin
from sorl.thumbnail import get_thumbnail

class DishCategoryInlineAdmin(AdminImageMixin, admin.TabularInline):
    model = DishCategory
    fields = ('name', 'position', 'status', )
    # define the sortable
    sortable_field_name = "position"
    extra = 0

class DishCategoryGroupAdmin(admin.ModelAdmin):
    list_display = ('name', )
        
    inlines = [DishCategoryInlineAdmin]


class DishInlineAdmin(AdminImageMixin, admin.TabularInline):
    model = Dish
    fields = ('title', 'position', 'status', )
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

class DishPriceAdmin(AdminImageMixin, admin.ModelAdmin):
    """docstring for DishAdmin"""

    pass

class DishPriceCategoryAdmin(AdminImageMixin, admin.ModelAdmin):
    """docstring for DishAdmin"""
    prepopulated_fields = {"slug": ("name",)}   
    
    pass
               

admin.site.register(DishCategoryGroup, DishCategoryGroupAdmin)
admin.site.register(DishCategory, DishCategoryAdmin)
admin.site.register(Dish, DishAdmin)
admin.site.register(DishPrice, DishPriceAdmin)
admin.site.register(DishPriceCategory, DishPriceCategoryAdmin)
