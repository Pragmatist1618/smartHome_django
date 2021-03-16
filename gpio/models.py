from django.db import models


class GPIO(models.Model):
    num = models.IntegerField()
    name = models.CharField(max_length=32, default='noname_gpio')
    state = models.BooleanField(default=False)

    def __str__(self):
        return "%s, %s, %s" % (self.name, self.num, self.state)