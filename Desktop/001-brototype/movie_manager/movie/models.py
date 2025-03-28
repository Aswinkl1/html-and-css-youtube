from django.db import models

# Create your models here.


class censorInfo(models.Model):
    rating = models.CharField(max_length = 40, null = True)
    centified_by = models.CharField(max_length = 250, null = True)

    def __str__(self):
        return self.centified_by

class directors(models.Model):
    name = models.TextField(max_length = 250, null = True)

    def __str__(self):
        return self.name

class Actor(models.Model):
    name = models.CharField(max_length = 250, null = True)

    def __str__(self):
        return self.name
    

class movie_info(models.Model):
    title = models.CharField(max_length = 250)
    year = models.IntegerField(null = True)
    plot = models.TextField()
    poster = models.ImageField(upload_to="images/", null=True)
    # one to one relation
    censor = models.OneToOneField(censorInfo, on_delete =models.SET_NULL, related_name = 'movie', null = True)
    #  one to many relation
    directed_by = models.ForeignKey(directors,null = True,on_delete = models.CASCADE,related_name= 'directed_movies')
    # many to many
    actors = models.ManyToManyField(Actor, related_name='acted_movies')
    



    def __str__(self):
        return self.title





