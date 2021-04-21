from django.db import models
import datetime
from django.utils import timezone


# Create your models here.
class Newsstuff(models.Model):
    pub_date = models.DateTimeField('date published')

    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)
