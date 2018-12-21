from django.db import models


class Product(models.Model):
    product_name = models.CharField(max_length=20)
    product_id = models.CharField(max_length=20, primary_key=True)

    def __str__(self):
        return 'Product:{} - ID:{}'.format(self.product_name, self.product_id)


class Location(models.Model):
    location_name = models.CharField(max_length=20)
    location_id = models.CharField(max_length=20, primary_key=True)

    def __str__(self):
        return '{} - ID:{}'.format(self.location_name, self.location_id)


class ProductMovement(models.Model):
    movement_id = models.IntegerField(primary_key=True)
    from_location = models.ForeignKey(
        'Location', on_delete=models.CASCADE, related_name='Location_at')
    to_location = models.ForeignKey(
        'Location', on_delete=models.CASCADE, related_name='Location_to_be')
    p_id = models.ForeignKey(
        'Product', on_delete=models.CASCADE, related_name='ProductMovement')
    timestamp = models.DateTimeField(auto_now_add=True)
    quantity = models.IntegerField(null=False)

    def __str__(self):
        return '{} - {} : ID = {}'.format(self.from_location, self.to_location, self.movment_id)
