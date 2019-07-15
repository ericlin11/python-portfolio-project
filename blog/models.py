from django.db import models

# Create a blog model

class Blog(models.Model):
    title = models.CharField(max_length = 255)
    pub_date = models.DateTimeField()
    image = models.ImageField(upload_to = 'images/')
    text = models.TextField(max_length=500)




# Add blog app to settings
# Create Migration
# Migrate
# Add to the admin
