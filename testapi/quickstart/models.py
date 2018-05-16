# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models


class Point(models.Model):
    x = models.IntegerField(default=0)
    y = models.IntegerField(default=0)
