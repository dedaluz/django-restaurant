from django.db import models



class ServiceQuerySet(models.query.QuerySet):
    def live(self):
        return self.filter(status__gte=2)
    
    def featured(self):
        return self.filter(status__gte=3)    

class PublicManager(models.Manager):
    """Returns published featured teasers."""
    
    use_for_related_fields = True
    
    def get_query_set(self):
        return ServiceQuerySet(self.model)
        
    def live(self, *args, **kwargs):
        return self.get_query_set().live(*args, **kwargs)
        
    def featured(self, *args, **kwargs):
        return self.get_query_set().featured(*args, **kwargs)
    