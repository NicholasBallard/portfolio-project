from django.db import models

class Blog(models.Model):
    title = models.CharField(max_length=300)
    pub_date = models.DateField(auto_now_add=True)    
    body = models.TextField()
    image = models.ImageField(upload_to='images/')

    # this makes the admin site display the title
    def __str__(self):
        return self.title

    def summary(self):
        return self.body[:200]
    
    # Don't need this since didn't use datetime
    # def pub_date_pretty(self):
    #     return self.pub_date.strftime('%m')

'''
Create a Blog model
--title
--pub_date
--body
--image



Create migration

Migrate

Add to the admin
'''


