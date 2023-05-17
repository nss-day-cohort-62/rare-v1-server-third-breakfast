from django.db import models

class Comment(models.Model):

    content = models.CharField(max_length=5000)
    created_on = models.DateTimeField()
    post = models.ForeignKey("Post", on_delete=models.CASCADE, related_name="post_comment")
    author = models.ForeignKey("RareUser", on_delete=models.CASCADE, related_name="comment_author")
