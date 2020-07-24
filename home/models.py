from django.db import models

# Create your models here.
class Contact(models.Model):
    sno = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    email = models.EmailField(max_length=50)
    content = models.TextField()
    timestamp = models.DateTimeField(auto_now=True, blank=True)

    def __str__(self):
        return 'Message From ' + self.name + ' - ' + self.email
        