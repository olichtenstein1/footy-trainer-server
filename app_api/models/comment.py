from django.db import models



class Comment(models.Model):

     post = models.ForeignKey("Post", on_delete=models.CASCADE)
     content = models.TextField()
     rating = models.IntegerField()
     footy_user = models.ForeignKey("FootyUser", on_delete=models.CASCADE)
     