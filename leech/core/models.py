from datetime import datetime
from urlparse import urlparse

from django.db import models


class Block(models.Model):
    owner = models.ForeignKey('auth.User')
    url = models.TextField()
    domain = models.CharField(max_length=255)
    when = models.DateTimeField(default=datetime.now)

    def save(self, *args, **kwargs):
        if not self.domain:
            self.domain = urlparse(self.url).netloc
        super(Block, self).save(*args, **kwargs)
