# from django.db import models
#
# class Symptoms(models.Model):
#     sympt = models.CharField(max_length=100)
#     sym = models.BooleanField()


from django.db import models
class Symptoms(models.Model):
    sympt = models.CharField(max_length=100)

class Post(models.Model):
    title=models.CharField(max_length=128)
    content=models.TextField()
    Cough = models.BooleanField()
    Fever = models.BooleanField()
    Runny_Nose = models.BooleanField()
    Nasal_Congestion = models.BooleanField()



    def __unicode__(self):
        return self.title

    def _str_(self):
        return self.title
