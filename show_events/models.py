from django.db import models


# Model for different categories
class Categories(models.Model):
    categories = models.CharField(max_length = 255)

    def __str__(self):
        return self.categories

# Model for different events
class Events(models.Model):
    title = models.CharField(max_length=255)
    image = models.ImageField(upload_to = 'Images/', blank =True, null = True, default = None)
    description = models.TextField()
    location = models.CharField(max_length = 255)
    categories = models.ManyToManyField(Categories, related_name = 'events')
    start_Date = models.DateTimeField()
    end_Date = models.DateTimeField()
    published = models.BooleanField(default = False)
    paid = models.BooleanField(default = False)

    # To sort events by date
    class Meta:
        ordering = ['-end_Date']

    def __str__(self):
        return self.title

    


# Model for tracking likes
class Likes(models.Model):
    event = models.OneToOneField(Events, on_delete = models.CASCADE)
    count = models.PositiveIntegerField()