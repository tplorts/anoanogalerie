from django.db import models
import json


# "Notation to Object"
def n2o( str_or_json ):
    try:
        data = json.loads( str_or_json )
    except ValueError:
        data = str_or_json
    return data



class Artist( models.Model ):
    name = models.CharField( max_length=200 )
    bio = models.TextField( blank=True )
    website = models.URLField( blank=True )
    email = models.EmailField( max_length=254, blank=True )

    def __unicode__(self):
        return self.name

    def ml_name(self):
        return n2o(self.name)

    def ml_bio(self):
        return n2o(self.bio)

    
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

    def ml_title(self):
        return n2o(self.title)

    def ml_brief(self):
        return n2o(self.brief)

    def ml_lengthy(self):
        return n2o(self.lengthy)

    def ml_hours(self):
        return n2o(self.hours)

    def ml_artist(self):
        return self.artist.ml_name()
