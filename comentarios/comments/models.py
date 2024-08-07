from django.db import models

class User(models.Model):
    username = models.CharField(max_length=255)

    def __str__(self):
        return self.username

class Post(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField()

    def __str__(self):
        return self.title

class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    text = models.TextField()

    def __str__(self):
        return f'{self.user.username} - {self.text[:20]}'
