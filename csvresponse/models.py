from uuid import uuid4
from django.db import models

class Deal(models.Model):
    uuid = models.UUIDField(primary_key=True, default=uuid4)
    customer = models.TextField()
    item = models.TextField()
    total = models.IntegerField()
    quantity = models.IntegerField()
    date = models.DateTimeField()
    index = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)

    @staticmethod
    def get_last_index():
        try:
            return Deal.objects.latest('created_at').index
        except Deal.DoesNotExist:
            return 1
