from django.db import models

class Post(models.Model):
    photo = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    title = models.CharField(max_length=100)
    description = models.TextField(null=True, blank=True)
    rate = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title


class Comment(models.Model):
    post = models.ForeignKey("post.Post", on_delete=models.CASCADE,
                             related_name="comments")
    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.text
