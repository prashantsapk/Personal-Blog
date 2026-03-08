from django.db import models
# Create your models here.

class Postathomepage(models.Model):
    title=models.TextField(max_length=100)
    image= models.ImageField(upload_to='')
    description=models.TextField(max_length=1000)

    def __str__(self):
        return self.title
    


#  A post can have many comments (one to many)
class commentofpost(models.Model):
    post=models.ForeignKey(Postathomepage,on_delete=models.CASCADE)
    comment=models.TextField() 