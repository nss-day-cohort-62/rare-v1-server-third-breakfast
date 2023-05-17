from django.db import models

class Subscription(models.Model):

    created_on = models.DateField()
    ended_on = models.DateField()
    follower = models.ForeignKey("RareUser", on_delete=models.CASCADE, related_name = "subscribed_follower")
    author = models.ForeignKey("RareUser", on_delete=models.CASCADE, related_name = "subscribed_author")
