from django.db import models
#import datetime

# Create your models here.

BLACKLISTED_SHORTCUT_NAMES = ("admin","api")

class shortcut(models.Model):
    shortcut_key = models.CharField(max_length=20,help_text="Key of the shortcut")
    shortcut_value = models.URLField(help_text="The target of the shortcut") # URL of the shortcut target
    shortcut_accesses = models.PositiveIntegerField(default=0) # Times the shortcut being accessed
    def __str__(self):
        return "{} -> {}, used {} time(s)".format(self.shortcut_key,self.shortcut_value,self.shortcut_accesses)
    def save(self, *args, **kwargs):
        if self.shortcut_key in BLACKLISTED_SHORTCUT_NAMES:
            return
        else:
            super().save(*args, **kwargs)


class log(models.Model):
    log_ip = models.TextField() # IP
    log_ua = models.TextField() # User Agent
    log_shortcut = models.TextField() # Requested shortcut
    log_time = models.DateTimeField(auto_now_add = True) # request time
    def __str__(self):
        return "{}: {} (UA {}) <- {}".format(str(self.log_time),self.log_ip,self.log_ua,self.log_shortcut)
