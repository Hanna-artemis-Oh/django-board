from django.db import models


class Post(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    author = models.CharField(max_length=50)
    created_at = models.DateTimeField('created date', auto_now_add=True)
    like = models.IntegerField(default=0)
    num_comments = models.IntegerField(default=0)

    def __str__(self):
        return self.title + " - " + self.author


class Comment(models.Model):
    author = models.CharField(max_length=50)
    content = models.CharField(max_length=200)
    created_at = models.DateTimeField('created date', auto_now_add=True)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)

    def __str__(self):
        return self.content + " - " + self.content
