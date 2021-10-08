from django.db import models


class Trainer(models.Model):
    first_name = models.CharField(max_length=30, blank=True)
    last_name = models.CharField(max_length=30, blank=True)
    subject = models.CharField(max_length=50)

    class Meta:
        db_table = 'trainer'

    def __str__(self):
        return '%s %s' % (self.first_name, self.last_name)
