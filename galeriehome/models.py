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


class Webshop(models.Model):
    exhibition = models.ForeignKey(
        Exhibition, null=True, blank=True,
        related_name='shops'
    )
    artist = models.ForeignKey(
        Artist, null=True, blank=True,
        related_name='shops'
    )
    directory = models.CharField(max_length=120)
    title = models.CharField(max_length=120, blank=True)
    about = models.TextField(blank=True)

    def __unicode__(self):
        if self.title is not None and len(self.title) > 0:
            return self.title
        if self.exhibition is not None:
            return unicode(self.exhibition)
        if self.artist is not None:
            return unicode(self.artist)
        return 'no title'

    def artistName(self):
        if self.artist is not None:
            return self.artist.ml_name()
        if self.exhibition is not None and self.exhibition.artist is not None:
            return self.exhibition.artist.ml_name()
        return ''

    def itemsOrdered(self):
        return self.items.order_by('ordinal')


class ShopItem(models.Model):
    shop = models.ForeignKey(Webshop, related_name='items')
    directory = models.CharField(max_length=120)
    ordinal = models.FloatField(null=True, blank=True)
    hasThumb = models.BooleanField(default=False)
    hasBig = models.BooleanField(default=False)
    name = models.CharField(max_length=120, blank=True)
    price = models.CharField(max_length=120, blank=True)
    info = models.TextField(blank=True)

    def __unicode__(self):
        return self.name

    def caption(self):
        return u'{} / {} / {}'.format(self.name, self.price, self.info)
