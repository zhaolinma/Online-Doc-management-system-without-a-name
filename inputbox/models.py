from django.db import models
from django.contrib.auth.models import User
class Article(models.Model):
    user = models.ForeignKey(User,default=1)
    title = models.CharField(max_length=100)
    sample_cover = models.FileField()
    def __str__(self):
        return self.title+' - '+self.user.username
    #E.G : Deep Learning - Zhaolin Ma
class Part(models.Model):
    Article = models.ForeignKey(Article, on_delete=models.CASCADE)
    type = models.CharField(max_length=50)
    text = models.CharField(max_length=2000)

    def __str__(self):
        return 'This is the '+self.type+' from '+self.Article.title
    #E.G : This is the introduction from Deep Learning

