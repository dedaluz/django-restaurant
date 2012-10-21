from django.contrib import admin
from services.models import Service, ServiceGroup
from sorl.thumbnail.admin import AdminImageMixin
from sorl.thumbnail import get_thumbnail

class DishInlineAdmin(AdminImageMixin, admin.TabularInline):
    model = Service
    fields = ('title', 'position', 'icon', 'status', )
    # define the sortable
    sortable_field_name = "position"
    extra = 0

class DishGroupAdmin(admin.ModelAdmin):
    list_display = ('name', )
    prepopulated_fields = {"slug": ("name",)} 
    
    inlines = [DishInlineAdmin]

class DishAdmin(AdminImageMixin, admin.ModelAdmin):
    """docstring for DishAdmin"""
    
    prepopulated_fields = {"slug": ("title",)}   
    list_display = ('title', 'position', 'status',)
    pass
        

admin.site.register(DishGroup, DishGroupAdmin)
admin.site.register(Dish, DishAdmin)
