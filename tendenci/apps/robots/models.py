from django.db import models

from tendenci.apps.robots.managers import RobotManager


STATUS_CHOICES = (('active','Active'),('inactive','Inactive'),)

class Robot(models.Model):
    name = models.CharField(max_length=150)
    url = models.URLField()
    version = models.CharField(max_length=50)
    status = models.NullBooleanField(default=True)
    status_detail = models.CharField(max_length=50, choices=STATUS_CHOICES,default='active')

    objects = RobotManager()

    def __unicode__(self):
        return self.name