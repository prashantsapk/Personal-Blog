from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Postathomepage(models.Model):
    title=models.TextField(max_length=100)
    image= models.ImageField(upload_to='')
    description=models.TextField(max_length=1000)
    user = models.ForeignKey(User,on_delete=models.CASCADE,related_name='posts')

    def __str__(self):
        return self.title
    


#  A post can have many comments (one to many)
class commentofpost(models.Model):
    post=models.ForeignKey(Postathomepage,on_delete=models.CASCADE,related_name='comments')
    comment=models.TextField()

    def __str__(self):
        return self.comment
    

# # A single post can have only one catageory at a time so we have to use One to one field here
    
class postcatageory(models.Model):
    post=models.OneToOneField(Postathomepage, on_delete=models.CASCADE)
    catageorychoices = [('Sports','Sports'),('Entertaintment','Entertaintment'),('News','News'),('Meme','Meme')]
    catageory = models.CharField(choices=catageorychoices)
    
    
    def __str__(self):
        return f'{self.catageory} - {self.post}'
