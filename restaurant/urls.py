from django.conf.urls.defaults import *
from services.models import *


service_list = {
    'queryset': Dish.objects.all(),
}


urlpatterns = patterns('django.views.generic.list_detail',
    url(r'^(?P<slug>[-\w]+)/$',
        view='object_detail',
        kwargs=service_list,
        name='service_detail',
    ),
    url (r'^$',
        view='object_list',
        kwargs=service_list,
        name='service_list',
    ),
)