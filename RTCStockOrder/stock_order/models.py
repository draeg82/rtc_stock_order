from django.db import models
from ordered_model.models import OrderedModel

class Item(OrderedModel):
    name = models.CharField(max_length=100)

    class Meta(OrderedModel.Meta):
        pass


class Washer(OrderedModel):
    washerName = models.CharField(max_length=30)

    def __str__(self):
        return self.washerName

    class Meta(OrderedModel.Meta):
        pass


class Product(OrderedModel):
    product = models.CharField(max_length=30)
    productType = models.CharField(max_length=30)

    def __str__(self):
        return self.product + ' - ' + self.productType

    class Meta(OrderedModel.Meta):
        pass



class WasherQueue(OrderedModel):
    washer = models.CharField(max_length=30)
    product = models.CharField(max_length=60)
    volume = models.CharField(max_length=10)

    def __str__(self):
        return self.washer + ': ' + self.product + ' - ' + self.volume

    class Meta(OrderedModel.Meta):
        pass
