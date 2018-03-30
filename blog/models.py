from django.db import models

class Blog(models.Model):
    title = models.CharField(max_length=300)
    pub_date = models.DateField(auto_now_add=True)    
    body = models.TextField()
    image = models.ImageField(upload_to='images/')

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


