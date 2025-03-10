from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser, Wallet, InvestmentPlan, InvestmentPurchase, ActiveInvestment, DepositWallet, WithdrawalTransaction
from django.utils.timezone import now


@admin.register(InvestmentPlan)
class InvestmentPlanAdmin(admin.ModelAdmin):
    list_display = ('name', 'amount', 'duration', 'created_at', 'expected_returns')  # Fields visible in the list view
    search_fields = ('name',)  # Allows searching by name
    list_filter = ('created_at',)  # Adds a filter for created_at
    ordering = ('-created_at',)  # Orders by newest first
    fieldsets = (
        (None, {
            'fields': ('name', 'description', 'amount', 'duration', 'expected_returns')
        }),
    )

@admin.register(InvestmentPurchase)
class InvestmentPurchaseAdmin(admin.ModelAdmin):
    list_display = ('user', 'plan', 'status', 'purchase_date', 'approved_at')
    list_filter = ('status',)
    actions = ["approve_selected", "reject_selected"]

    def approve_selected(self, request, queryset):
        """Approve selected investments and move them to ActiveInvestment."""
        for purchase in queryset:
            if purchase.status == "pending":  # Ensure it’s not already approved
                purchase.approve()
        self.message_user(request, "Selected investments have been approved.")

    def reject_selected(self, request, queryset):
        """Reject selected investments."""
        for purchase in queryset:
            if purchase.status == "pending":  # Ensure it’s not already rejected
                purchase.reject()
        self.message_user(request, "Selected investments have been rejected.")

    approve_selected.short_description = "Approve selected investments"
    reject_selected.short_description = "Reject selected investments"

@admin.register(ActiveInvestment)
class ActiveInvestmentAdmin(admin.ModelAdmin):
    """Admin panel for managing active investments."""
    list_display = ("user", "plan", "date_activated")
    actions = ["delete_selected"]

    def delete_selected(self, request, queryset):
        """Allow admin to delete active investments."""
        queryset.delete()
        self.message_user(request, "Selected active investments deleted.")

    delete_selected.short_description = "Delete selected active investments"




class CustomUserAdmin(UserAdmin):
    list_display = ('username', 'email', 'user_type', 'is_active', 'is_staff')
    list_filter = ('user_type', 'is_active', 'is_staff')
    search_fields = ('username', 'email')
    ordering = ('username',)

admin.site.register(CustomUser, CustomUserAdmin)

class WalletAdmin(admin.ModelAdmin):
    list_display = ('user', 'balance')
    search_fields = ('user__username', 'user__email')
    list_filter = ('user',)

# Check if Wallet is already registered
if Wallet not in admin.site._registry:
    admin.site.register(Wallet, WalletAdmin)

@admin.register(DepositWallet)
class DepositWalletAdmin(admin.ModelAdmin):
    list_display = ("name", "address", "updated_at")
    list_editable = ("address",)  # Allows inline editing of addresses
    ordering = ("name",)

    def has_add_permission(self, request):
        """Prevent admin from adding new cryptocurrency types."""
        return False  # Disables the 'Add' button

    def has_delete_permission(self, request, obj=None):
        """Prevent admin from deleting cryptocurrencies."""
        return False  # Disables the delete option

@admin.register(WithdrawalTransaction)
class WithdrawalTransactionAdmin(admin.ModelAdmin):
    list_display = ("user", "crypto_type", "amount", "withdrawal_address", "status", "request_date", "processed_at")
    list_filter = ("status", "crypto_type")
    search_fields = ("user__username", "withdrawal_address")
    actions = ["approve_selected", "reject_selected"]

    def approve_selected(self, request, queryset):
        for withdrawal in queryset:
            if withdrawal.status == "pending":
                withdrawal.status = "approved"
                withdrawal.processed_at = now()
                withdrawal.save()
        self.message_user(request, "Selected withdrawals have been approved.")

    def reject_selected(self, request, queryset):
        for withdrawal in queryset:
            if withdrawal.status == "pending":
                withdrawal.status = "rejected"
                withdrawal.processed_at = now()
                withdrawal.save()
        self.message_user(request, "Selected withdrawals have been rejected.")

    approve_selected.short_description = "Approve selected withdrawals"
    reject_selected.short_description = "Reject selected withdrawals"