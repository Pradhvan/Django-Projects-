from rest_framework import generics
# for one or many filter option
from django_filters import rest_framework
from .models import branch, bank
from .serializers import BranchSerializer, BankSerializer


class BranchFilter(rest_framework.FilterSet):

    class Meta:
        model = branch
        fields = ('bank', 'city', 'ifsc')


class BranchapiView(generics.ListAPIView):
    queryset = branch.objects.all()
    serializer_class = BranchSerializer
    filterset_class = BranchFilter


class BankapiView(generics.ListAPIView):
    queryset = bank.objects.all()
    serializer_class = BankSerializer
