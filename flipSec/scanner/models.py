from django.db import models

# Create your models here.
class ArpScan(models.Model):
    ip = models.CharField(max_length=255, verbose_name='IP Address')
    mac = models.CharField(max_length=60, verbose_name='MAC Address')
    host = models.CharField(max_length=50, verbose_name='HostName')
    domain = models.CharField(max_length=100, verbose_name='Domain Name')
    os = models.CharField(max_length=20, verbose_name='Operating System')
