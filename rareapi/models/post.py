from django.db import models

class Post(models.Model):

    user = models.ForeignKey("RareUser", on_delete=models.CASCADE)
    category = models.ForeignKey("Category", on_delete=models.CASCADE)
    title = models.CharField(max_length=30)
    publication_date = models.DateField()
    image_url = models.URLField()
    content = models.CharField(max_length=300)
    approved = models.BooleanField()
    post_tags = models.ManyToManyField("Tag")
    post_reaction = models.ManyToManyField("Reaction")
