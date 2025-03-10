from django.contrib.auth.models import AbstractUser, User
from django.db import models
from django.conf import settings




class InvestmentPlan(models.Model):
    name = models.CharField(max_length=255, unique=True)
    description = models.TextField()
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    expected_returns = models.DecimalField(max_digits=10, decimal_places=2, default=10)  # Add default
    duration = models.PositiveIntegerField(help_text="Duration in days")
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} - {self.amount} USD"

    def calculate_expected_earnings(self):
        return (self.amount * self.expected_returns) / 100

class InvestmentPurchase(models.Model):
    STATUS_CHOICES = [
        ('pending', 'Pending'),
        ('approved', 'Approved'),
        ('rejected', 'Rejected'),
    ]

    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    plan = models.ForeignKey(InvestmentPlan, on_delete=models.CASCADE)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='pending')
    purchase_date = models.DateTimeField(auto_now_add=True)
    approved_at = models.DateTimeField(null=True, blank=True)

    def approve(self):
        """Approve investment and move it to ActiveInvestment."""
        self.status = "Approved"
        self.save()
        ActiveInvestment.objects.create(user=self.user, plan=self.plan)

    def reject(self):
        """Reject investment."""
        self.status = "Rejected"
        self.save()

    def __str__(self):
        return f"{self.user.username} - {self.plan.name} ({self.status})"


class ActiveInvestment(models.Model):
    """Stores only approved investments."""
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    plan = models.ForeignKey(InvestmentPlan, on_delete=models.CASCADE)
    date_activated = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username} - {self.plan.name} (Active)"




class Wallet(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    balance = models.DecimalField(max_digits=12, decimal_places=2, default=0.00)

    def __str__(self):
        return f"{self.user.username}'s Wallet - Balance: {self.balance}"

class Transaction(models.Model):
    TRANSACTION_TYPES = [
        ('deposit', 'Deposit'),
        ('withdrawal', 'Withdrawal'),
    ]

    wallet = models.ForeignKey(Wallet, on_delete=models.CASCADE)
    transaction_type = models.CharField(max_length=10, choices=TRANSACTION_TYPES)
    amount = models.DecimalField(max_digits=12, decimal_places=2)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.wallet.user.username} - {self.transaction_type} - {self.amount}"

class CustomUser(AbstractUser):
    USER_TYPE_CHOICES = (
        ('client', 'Client'),
        ('admin', 'Admin'),
    )
    user_type = models.CharField(max_length=10, choices=USER_TYPE_CHOICES, default='client')

class DepositWallet(models.Model):
    CRYPTO_CHOICES = [
        ("Bitcoin", "Bitcoin"),
        ("Ethereum", "Ethereum"),
        ("USDT_BEP20", "USDT BEP20"),
        ("USDT_ERC20", "USDT ERC20"),
        ("USDT_TRC20", "USDT TRC20"),
    ]

    name = models.CharField(max_length=20, choices=CRYPTO_CHOICES, unique=True)
    address = models.CharField(max_length=255)  # Admin updates this
    updated_at = models.DateTimeField(auto_now=True)

    def str(self):
        return f"{self.get_name_display()} - {self.address}"


class WithdrawalTransaction(models.Model):
    CRYPTO_CHOICES = [
        ('bitcoin', 'Bitcoin'),
        ('ethereum', 'Ethereum'),
        ('usdt_bep20', 'USDT BEP20'),
        ('usdt_erc20', 'USDT ERC20'),
        ('usdt_trc20', 'USDT TRC20'),
    ]

    STATUS_CHOICES = [
        ('pending', 'Pending'),
        ('approved', 'Approved'),
        ('rejected', 'Rejected'),
    ]

    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    crypto_type = models.CharField(max_length=20, choices=CRYPTO_CHOICES)
    withdrawal_address = models.CharField(max_length=255)
    amount = models.DecimalField(max_digits=12, decimal_places=2)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='pending')
    request_date = models.DateTimeField(auto_now_add=True)
    processed_at = models.DateTimeField(null=True, blank=True)

class UserProfile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    profile_picture = models.ImageField(upload_to="profile_pics/", null=True, blank=True)

    def str(self):
        return self.user.username