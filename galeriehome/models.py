from django.db import models

class Artist( models.Model ):
    name = models.CharField( max_length=200 )
    bio = models.TextField( blank=True )
    website = models.URLField( blank=True )
    email = models.EmailField( max_length=254, blank=True )

    def __unicode__(self):
        return self.name

    
class Exhibition( models.Model ):
    title = models.CharField( max_length=200 )
    brief = models.CharField( max_length=300, blank=True )
    lengthy = models.TextField( blank=True )
    start = models.DateField()
    end = models.DateField()
    hours = models.TextField()
    artist = models.ForeignKey( Artist, null=True, blank=True )
    picture = models.URLField( blank=True )

    def __unicode__(self):
        return self.title
