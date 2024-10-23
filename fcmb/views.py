from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.decorators import action
from django.shortcuts import get_object_or_404

from .models import Customer, Account, Transaction
from .serializers import CustomerSerializer, AccountSerializer, TransactionSerializer

class CustomerViewSet(viewsets.ModelViewSet):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer


class AccountViewSet(viewsets.ModelViewSet):
    queryset = Account.objects.all()
    serializer_class = AccountSerializer

    # Custom action to query by account number
    @action(detail=False, methods=['get'], url_path='by-account-number/(?P<account_number>[^/.]+)')
    def get_by_account_number(self, request, account_number=None):
        account = get_object_or_404(Account, account_number=account_number)
        serializer = self.get_serializer(account)
        return Response(serializer.data)


class TransactionViewSet(viewsets.ModelViewSet):
    queryset = Transaction.objects.all()
    serializer_class = TransactionSerializer

    # Custom action to get transactions by account number
    @action(detail=False, methods=['get'], url_path='by-account-number/(?P<account_number>[^/.]+)')
    def get_by_account_number(self, request, account_number=None):
        transactions = Transaction.objects.filter(account__account_number=account_number)
        serializer = self.get_serializer(transactions, many=True)
        return Response(serializer.data)
