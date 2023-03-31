from django.db import models


class SingleActive(models.Model):
    active = models.BooleanField(default=True)

    class Meta:
        abstract = True

    def save(self, *args, **kwargs):
        if self.active:
            self.__class__.objects.filter(active=True).update(active=False)
        return super(SingleActive, self).save(*args, **kwargs)
