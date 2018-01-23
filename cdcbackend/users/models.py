import binascii
import os

from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    token = models.CharField(max_length=40)

    def save(self, *args, **kwargs):
        if not self.token:
            self.token = binascii.hexlify(os.urandom(20)).decode()
        return super().save(*args, **kwargs)


class OwnedModel(models.Model):
    owned_by = models.ForeignKey('users.User', null=True, on_delete=models.deletion.DO_NOTHING)

    class Meta:
        abstract = True
