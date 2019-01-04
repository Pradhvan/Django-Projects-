from django.db import models


class bank(models.Model):
    name = models.CharField(max_length=50, unique=True)
    bkid = models.IntegerField(primary_key=True)

    def __str__(self):
        return '{} {}'.format(self.name, self.bkid)


class branch(models.Model):
    ifsc = models.CharField(max_length=11, primary_key=True)
    bank = models.ForeignKey(
        'bank', on_delete=models.CASCADE, related_name="branch")
    branch_name = models.CharField(max_length=15)
    address = models.TextField(max_length=1500)
    city = models.CharField(max_length=12)
    district = models.CharField(max_length=12)
    state = models.CharField(max_length=12)

    def __str__(self):
        return ' BRANCH: {} ---- IFSC: {}'.format(self.branch_name, self.ifsc)
