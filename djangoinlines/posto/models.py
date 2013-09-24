from django.db import models

class Posto(models.Model):
    name = models.CharField("name", max_length=255)
    
    def __unicode__(self):
        return self.name

class Bomba(models.Model):
    posto = models.ForeignKey(Posto)
    name = models.CharField("name", max_length=255)
    
    def __unicode__(self):
        return self.name
        
class Bico(models.Model):
    bomba = models.ForeignKey(Bomba)
    name = models.CharField("name", max_length=255)
    
    def __unicode__(self):
        return self.name
        
