from datetime import datetime
from django.db import models


class AbstractTemporalModel(models.Model):
    """
    This is the abstract model that adds two datetime fields to all the temporal models.
    """

    StartTimeStamp = models.DateTimeField(auto_now_add=True)
    EndTimeStamp = models.DateTimeField(
        default=datetime(year=9999, month=12, day=31, hour=23, minute=59, second=59, microseconds=999999))

    class Meta:
        abstract = True
