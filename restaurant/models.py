from django.db import models
from django.utils.translation import ugettext_lazy as _
from sorl.thumbnail import ImageField
from django.db.models import permalink

from managers import PublicManager


from django.db import models
from django.utils.translation import ugettext_lazy as _
from sorl.thumbnail import ImageField
from flexslider.models import Slider
from django.db.models import permalink

from managers import PublicManager

class DishCategoryGroup(models.Model):
    """docstring for CategoryGroup"""
    name = models.CharField(_('name'), max_length=100)
    class Meta:
        verbose_name = u'Dish Category Group'
        verbose_name_plural = u'Dish Category Groups'
    
    def __unicode__(self):
        return self.name
        


class DishCategory(models.Model):
    STATUS_CHOICES = (
        (0, _('Private')),
        (1, _('Draft')),
        (2, _('Public')),
        (3, _('Featured')),
    )
    category_group = models.ForeignKey(DishCategoryGroup)
    parent = models.ForeignKey('self', related_name='children', blank=True, null=True)
    name = models.CharField(_("name"), max_length=100)
    slug = models.SlugField()
    caption = models.TextField(_('caption'), blank=True)
    description = models.TextField(_('description'), blank=True)
    
    
    # images
    picture  = ImageField(_('picture'), upload_to='restaurant/categories/', blank=True, null=True)
    
    # position field
    position = models.PositiveSmallIntegerField("Position", default=0)
    status  = models.IntegerField(_('status'), choices=STATUS_CHOICES, default=2)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    
    class Meta:
        verbose_name = u'Category'
        verbose_name_plural = u'Categories'
        ordering = ('position',)
        unique_together = ('slug', 'parent',)
    
    def __unicode__(self):
        if self.parent:
          return u'%s: %s - %s' % (self.parent.name,
                                   self.name)
        return u'%s' % (self.name)
        
class Dish(models.Model):
    """
    (Featured description)
    """
    STATUS_CHOICES = (
        (0, _('Private')),
        (1, _('Draft')),
        (2, _('Public')),
        (3, _('Featured')),
    )
    category = models.ForeignKey(DishCategory, related_name="dish_categories")
    title = models.CharField(_('title'), max_length=200)
    slug = models.SlugField(unique=True)
    caption = models.TextField(_('caption'), blank=True)
    excerpt = models.TextField(_('excerpt'), blank=True)
    description = models.TextField(_('description'), blank=True)
    ingredients = models.TextField(_('ingredients'), blank=True)
    notes = models.TextField(_('notes'), blank=True)
    is_vegetarian = models.NullBooleanField(_('is_vegetarian'),)
    contains_gluten = models.NullBooleanField(_('contains gluten'),)
    is_speciality = models.NullBooleanField(_('is speciality'),)
    origin = models.CharField(blank=True, null=True, max_length=200)
    
    slider = models.ForeignKey(Slider, blank=True, null=True, related_name="dish_slider")  
    status  = models.IntegerField(_('status'), choices=STATUS_CHOICES, default=2)
    
    # position field
    position = models.PositiveSmallIntegerField("Position", default=0)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    objects = PublicManager()
    
    class Meta:
        verbose_name = u'Dish'
        verbose_name_plural = u'Dishes'
        ordering = ('position',)
    
    def __unicode__(self):
        return self.title

    @permalink
    def get_absolute_url(self):
        return ('dish_detail', None, { 'slug':self.slug })

class DishPriceCategory(models.Model):
    name = models.CharField(max_length=150)
    slug = models.SlugField(unique=True)
        
    class Meta:
        verbose_name = u'Price Category'
        verbose_name_plural = u'Price Categories'
    
    def __unicode__(self):
        return self.name

    
class DishPrice(models.Model):
    STATUS_CHOICES = (
        (0, _('Private')),
        (1, _('Draft')),
        (2, _('Public')),
        (3, _('Featured')),
    )
    dish = models.ForeignKey(Dish, related_name='prices')
    category = models.ForeignKey(DishPriceCategory, blank=True, null=True)
    price = models.DecimalField(_('price'), max_digits=6, decimal_places=2)
    notes = models.TextField(_('price notes'), blank=True)
    status  = models.IntegerField(_('status'), choices=STATUS_CHOICES, default=2)
     
    class Meta:
        verbose_name = u'Price'
        verbose_name_plural = u'Prices'
        ordering = ('price',)
    
    def __unicode__(self):
        return  u'%s (%s): %0.2f ' % (self.dish, self.category, self.price)
    
    
    