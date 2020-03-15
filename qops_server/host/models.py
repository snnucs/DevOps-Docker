from django.db import models
from django.utils.translation import gettext_lazy as _


class Host(models.Model):
    name = models.CharField(max_length=50)
    category = models.CharField(max_length=50, verbose_name=_('host category'))
    hostname = models.CharField(max_length=50, verbose_name=_('host name'))
    port = models.IntegerField(verbose_name=_('host port'), default=22)
    username = models.CharField(max_length=50, verbose_name=_('username'))
    desc = models.CharField(max_length=255, null=True, blank=True)

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'hosts'
        verbose_name = _('host')
        verbose_name_plural = verbose_name
        ordering = ('-id', )
