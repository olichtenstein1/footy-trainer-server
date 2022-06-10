from django.db import models



class Post(models.Model):

     footy_user = models.ForeignKey("FootyUser", on_delete=models.CASCADE)
     difficulty_level = models.IntegerField()
     description = models.TextField()
     title = models.TextField()
     video_tutorial = models.URLField(max_length=200)
     topic = models.ForeignKey("Topic", on_delete=models.CASCADE)
     category = models.ManyToManyField("Category", through="PostCategories", related_name="posts")