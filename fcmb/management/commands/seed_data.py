import random
from datetime import timedelta
from django.utils import timezone
from fcmb.models import Customer, Account, Transaction

from django.core.management.base import BaseCommand


class Command(BaseCommand):
    help = 'Seed the database with test data'

    def handle(self, *args, **kwargs):
        seed_data()
        self.stdout.write(self.style.SUCCESS('Database seeded successfully!'))


def seed_data():
    # Nigerian customer details
    customers_data = [
        {
            'customer_id': 'CUST001',
            'first_name': 'Chinwe',
            'last_name': 'Okonkwo',
            'gender': 'F',
            'date_of_birth': '1985-04-21',
            'email': 'chinwe.okonkwo@gmail.com',
            'contact_number': '+2348012345678',
            'address': '12, Bode Thomas, Surulere, Lagos'
        },
        {
            'customer_id': 'CUST002',
            'first_name': 'Adeola',
            'last_name': 'Olawale',
            'gender': 'M',
            'date_of_birth': '1990-07-13',
            'email': 'adeola.olawale@gmail.com',
            'contact_number': '+2348034567890',
            'address': '15, Marina, Lagos Island, Lagos'
        },
        {
            'customer_id': 'CUST003',
            'first_name': 'Aisha',
            'last_name': 'Abubakar',
            'gender': 'F',
            'date_of_birth': '1988-09-09',
            'email': 'aisha.abubakar@gmail.com',
            'contact_number': '+2348076543210',
            'address': '45, Sultan Road, Kaduna'
        },
    ]

    # Account types
    account_types = ['savings', 'current', 'business']

    # Seed customers
    customers = []
    for customer_data in customers_data:
        customer, created = Customer.objects.get_or_create(
            customer_id=customer_data['customer_id'],
            defaults=customer_data
        )
        customers.append(customer)

    # Seed accounts
    accounts = []
    for customer in customers:
        for i in range(1, 3):  # Each customer gets 2 accounts
            account_number = f"{random.randint(1000000000, 9999999999)}"
            account = Account.objects.create(
                account_number=account_number,
                account_name=f"{customer.first_name} {customer.last_name}",
                customer=customer,
                balance=round(random.uniform(50000, 500000), 2),
                account_type=random.choice(account_types)
            )
            accounts.append(account)

    # Seed transactions
    for account in accounts:
        for _ in range(5):  # Each account gets 5 transactions
            Transaction.objects.create(
                account=account,
                amount=round(random.uniform(5000, 20000), 2),
                transaction_type=random.choice(['debit', 'credit']),
                description=f"Transaction for account {account.account_number}",
                timestamp=timezone.now() - timedelta(days=random.randint(1, 30))  # Random past date
            )

    print(f"Seeded {len(customers)} customers, {len(accounts)} accounts, and {len(accounts) * 5} transactions.")


