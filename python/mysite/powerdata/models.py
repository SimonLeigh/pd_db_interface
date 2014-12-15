# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Remove `managed = False` lines for those models you wish to give write DB access
# Feel free to rename the models, but don't rename db_table values or field names.
#
# Also note: You'll have to insert the output of 'django-admin.py sqlcustom [appname]'
# into your database.
from __future__ import unicode_literals
import time
from datetime import datetime

from django.db import models

class SCPMmeasurement(models.Model):
    class Meta:
        managed = False
        db_table = 'scpm_measurements'

    unix_time = models.DecimalField(primary_key=True, max_digits=12, decimal_places=1)
    active_power = models.DecimalField(max_digits=8, decimal_places=2, blank=True, null=True)
    apparent_power = models.DecimalField(max_digits=8, decimal_places=2, blank=True, null=True)
    voltage = models.DecimalField(max_digits=6, decimal_places=2, blank=True, null=True)

    def __unicode__(self):
        ''' Returns string representation of a measurement '''
        return 'T: {0}, Act: {1}, App: {2}, V: {3}'.format(
            datetime.utcfromtimestamp(self.unix_time),
            unicode(self.active_power),
            unicode(self.apparent_power),
            unicode(self.voltage))

    def is_recent(self):
        ''' Returns last x hours of data '''
        return self.unix_time >= int(datetime.time())-(3600)



