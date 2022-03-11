from django.contrib import admin
from .models import Categories, Events, Likes


# Register models
admin.site.register(Categories)
admin.site.register(Events)
admin.site.register(Likes)