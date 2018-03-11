from django.db import models


# Create your models here.

#ovo je tabela u bazi
class Hashtag(models.Model):
    h_name = models.CharField(max_length=100)

#ovo je tabela u bazi
class Tweet(models.Model):

    screen_name = models.CharField(max_length=100) #Tweeter korisnik
    text = models.CharField(max_length=140)
    hashtags = models.ManyToManyField(
        Hashtag,
        through='veznatabela',
        through_fields=('tweet', 'hashtag')

    )
    created_at = models.DateField() #datum
    is_retweet = models.BooleanField() #retweetovao sam
    #geo_lokacija =
    def __str__(self):
        sep = ' '
        s = (str(self.screen_name) + sep + str(self.text) + sep  + '\n')
        return(s)

class Veznatabela(models.Model):
    tweet = models.ForeignKey(Tweet, on_delete=models.CASCADE)
    hashtag = models.ForeignKey(Hashtag, on_delete=models.CASCADE)


