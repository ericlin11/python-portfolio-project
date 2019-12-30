from django.db import models

# Create a blog model

class Blog(models.Model):
    title = models.CharField(max_length = 255)
    pub_date = models.DateTimeField()
    image = models.ImageField(upload_to = 'images/')
    text = models.TextField(max_length=500)


    def __str__(self):
        return self.title

    def summary(self):
        length_of_text = len(self.text)
        info = (self.text[:100] + "...") if (length_of_text > 100) else (self.text[:100])
        return info

    def pub_date_pretty(self):
        return self.pub_date.strftime('%b %e, %Y')
