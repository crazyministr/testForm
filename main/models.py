from django.db import models


class User(models.Model):
    name = models.CharField(max_length=13, default='')
    salary = models.PositiveIntegerField(default=0)

    def __unicode__(self):
        return u'%s %d' % (self.name, self.salary)

    class Meta:
        app_label = 'main'
