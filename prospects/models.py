from django.db import models
from django.utils.translation import ugettext as _

from prospects.validators import rfc_validator


class Prospects(models.Model):
    class Status(models.IntegerChoices):
        SENT = 0
        AUTHORIZED = 1
        REJECTED = 2

    name = models.CharField(max_length=80, verbose_name=_('name'))
    first_lastname = models.CharField(max_length=50, verbose_name=_('first lastname'))
    second_lastname = models.CharField(max_length=50, verbose_name=_('second lastname'), blank=True, null=True)
    street = models.CharField(max_length=80, verbose_name=_('street'))
    number = models.CharField(max_length=10, verbose_name=_('number'))
    suburb = models.CharField(max_length=80, verbose_name=_('suburb'))
    zip_code = models.CharField(max_length=10, verbose_name=_('zip code'))
    phone = models.CharField(max_length=15, verbose_name=_('phone'))
    rfc = models.CharField(max_length=13, verbose_name=_('rfc'), validators=[rfc_validator])
    status = models.PositiveIntegerField(choices=Status.choices, default=Status.SENT, verbose_name=_('status'))
    reject_details = models.CharField(max_length=200, verbose_name=_('reject details'), blank=True, null=True)

    class Meta:
        default_related_name = 'prospects'
        verbose_name = _('prospect')
        verbose_name_plural = _('prospects')

    def __str__(self):
        return '%s %s %s' % (self.name, self.first_lastname, self.second_lastname)

    def get_status_value(self):
        values = {
            0: _('Sent'),
            1: _('Authorized'),
            2: _('Rejected'),
        }
        return values[self.status]


class Documents(models.Model):
    name = models.CharField(max_length=100, verbose_name=_('name'))
    file = models.FileField(verbose_name=_('document'), upload_to='documents/')
    prospect = models.ForeignKey(Prospects, on_delete=models.CASCADE)

    class Meta:
        default_related_name = 'documents'
        verbose_name = _('document')
        verbose_name_plural = _('documents')

    def __str__(self):
        return '%s -> %s' % (self.name, self.prospect)
