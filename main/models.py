from django.db import models

# Create your models here.

class shortcut(models.Model):
    shortcut_key = models.TextField()
    shortcut_value = models.URLField() # URL of the shortcut target
    shortcut_accesses = models.PositiveIntegerField() # Times the shortcut being accessed
    def __str__(self):
        return "{} -> {}, used {} time(s)".format(self.shortcut_key,self.shortcut_value,self.shortcut_accesses)
