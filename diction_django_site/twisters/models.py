from django.db import models


class Twister(models.Model):
    twister = models.TextField('tongue twister', unique=True, null=False)
    source = models.TextField('source')

    class Meta:
        db_table = "twisters"

