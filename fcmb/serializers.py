from rest_framework import serializers
from .models import Customer, Account, Transaction

class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = '__all__'

class AccountSerializer(serializers.ModelSerializer):
    customer = CustomerSerializer(read_only=True)  

    class Meta:
        model = Account
        fields = '__all__'

class TransactionSerializer(serializers.ModelSerializer):
    account = AccountSerializer(read_only=True)  

    class Meta:
        model = Transaction
        fields = '__all__'
