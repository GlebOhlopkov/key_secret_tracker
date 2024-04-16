from datetime import datetime

from django.db import models


class Secret(models.Model):
    LIFETIME = [
        ('30_min', '30 minutes'),
        ('1_hour', '1 hour'),
        ('4_hour', '4 hours'),
        ('12_hour', '12 hours'),
        ('1_day', '1 day'),
        ('7_day', '7 days'),
    ]
    text = models.TextField(verbose_name='Secret text')
    key = models.CharField(max_length=255, unique=True, verbose_name='Secret key')
    secret_key = models.CharField(max_length=50, blank=True, null=True, verbose_name='Secret key for open Secret')
    lifetime = models.CharField(max_length=10, choices=LIFETIME, default='1_hour', verbose_name='Lifetime of Secret')
    created_at = models.DateTimeField(auto_now=True, verbose_name='Created at')
    is_open = models.BooleanField(default=False, verbose_name='is Open')

    def __str__(self):
        return f'{self.key}: {self.created_at}, {self.lifetime}'

    class Meta:
        verbose_name = 'Secret'
        verbose_name_plural = 'Secrets'
