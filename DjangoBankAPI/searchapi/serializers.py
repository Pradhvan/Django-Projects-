from rest_framework import serializers

from .models import branch, bank


class BankSerializer(serializers.ModelSerializer):
    class Meta:
        model = bank
        fields = ('name', 'bkid')


class BranchSerializer(serializers.ModelSerializer):

    bank = BankSerializer(read_only=True)

    class Meta:
        model = branch
        fields = ('bank', 'ifsc', 'branch_name', 'address',
                  'city', 'district', 'state',)
