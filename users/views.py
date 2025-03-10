from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login, logout
from .forms import CustomUserCreationForm, WithdrawalForm, ProfileUpdateForm, ProfilePictureForm
from django.contrib.auth.views import LoginView
from django.contrib.auth.decorators import login_required
from .models import Wallet, InvestmentPlan, InvestmentPurchase, Transaction, ActiveInvestment, DepositWallet, WithdrawalTransaction, UserProfile
from django.urls import reverse
from django.utils.timezone import now
from django.contrib import messages

def user_logout(request):
    logout(request)
    return redirect("login")

@login_required
def wallet_dashboard(request):
    wallet, created = Wallet.objects.get_or_create(user=request.user)
    transactions = Transaction.objects.filter(wallet=wallet).order_by('-timestamp')

    return render(request, 'users/wallet_dashboard.html', {
        'wallet': wallet,
        'transactions': transactions
    })

class CustomLoginView(LoginView):
    template_name = "users/login.html"

def home(request):
    return render(request, "base.html")

def contact(request):
    return render(request, "users/contact.html")
def about(request):
    return render(request, "users/about.html")

def register(request):
    if request.method == "POST":
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.user_type = "client"  # Force all signups to be clients
            user.save()
            login(request, user)
            # Use reverse to ensure the URL name matches your URLconf
            return redirect(reverse("dashboard"))
    else:
        form = CustomUserCreationForm()
    return render(request, "users/register.html", {"form": form})

class CustomLoginView(LoginView):
    template_name = "users/login.html"

    def get_success_url(self):
        user = self.request.user
        if user.is_authenticated:
            if user.user_type == "admin":
                return reverse("admin:index")  # Using the admin URL name
            else:
                return reverse("dashboard")     # Ensure this name exists in urls.py
        return super().get_success_url()


@login_required
def client_dashboard(request):
    user = request.user
    wallet, created = Wallet.objects.get_or_create(user=user)
    investment_plans = InvestmentPlan.objects.all()  # Fetch all available investment plans
    active_investments = ActiveInvestment.objects.filter(user=user)  # Fetch user's active investments

    context = {
        "wallet": wallet,
        "investment_plans": investment_plans,
        "active_investments": active_investments,
    }
    return render(request, "users/client_dashboard.html", context)



@login_required
def transaction(request):
    return render(request, "users/transaction.html")


@login_required
def purchase_plan(request):
    """
    Combined view for selecting an investment plan and confirming the purchase.

    GET:
      - If 'plan_id' is provided in the query parameters, display confirmation details.
      - Otherwise, show a list of available plans.
      - In both cases, deposit_wallets is passed to populate the dropdown.

    POST:
      - Create a pending InvestmentPurchase for the selected plan and redirect to dashboard.
    """
    if request.method == "GET":
        deposit_wallets = DepositWallet.objects.all()
        plan_id = request.GET.get("plan_id")
        if plan_id:
            plan = get_object_or_404(InvestmentPlan, id=plan_id)
            expected_earnings = None
            if hasattr(plan, "calculate_expected_earnings"):
                expected_earnings = plan.calculate_expected_earnings()
            return render(request, "users/confirm_purchase.html", {
                "plan": plan,
                "expected_earnings": expected_earnings,
                "deposit_wallets": deposit_wallets,
            })
        else:
            plans = InvestmentPlan.objects.all()
            return render(request, "users/confirm_purchase.html", {
                "plans": plans,
                "deposit_wallets": deposit_wallets,
            })

    elif request.method == "POST":
        plan_id = request.POST.get("plan_id")
        plan = get_object_or_404(InvestmentPlan, id=plan_id)
        InvestmentPurchase.objects.create(
            user=request.user,
            plan=plan,
            status="pending"  # status set to pending
        )
        messages.success(request, "Your investment purchase request has been submitted for approval.")
        return redirect("pending")
@login_required
def purchase_success(request):
    return render(request, "users/purchase_success.html")

@login_required
def pending(request):
    return render(request, "users/pending.html")

@login_required
def withdraw(request):
    # Retrieve the wallet for the current user.
    wallet = get_object_or_404(Wallet, user=request.user)
    # Get the transaction history for this user.
    transactions = WithdrawalTransaction.objects.filter(user=request.user).order_by('-request_date')

    if request.method == 'POST':
        form = WithdrawalForm(request.POST)
        if form.is_valid():
            amount = form.cleaned_data['amount']
            if wallet.balance >= amount:
                # Deduct the withdrawal amount from wallet.
                wallet.balance -= amount
                wallet.save()

                # Create a pending withdrawal transaction.
                withdrawal = form.save(commit=False)
                withdrawal.user = request.user
                withdrawal.status = 'pending'
                withdrawal.save()

                messages.success(request, "Withdrawal request submitted and is pending approval.")
                return redirect('withdraw')
            else:
                messages.error(request, "Insufficient balance for this withdrawal.")
    else:
        form = WithdrawalForm()

    context = {
        'form': form,
        'wallet': wallet,
        'transactions': transactions,
    }
    return render(request, "users/withdraw.html", context)

@login_required
def profile(request):
    user_profile, created = UserProfile.objects.get_or_create(user=request.user)

    if request.method == "POST":
        user_form = ProfileUpdateForm(request.POST, instance=request.user)
        profile_form = ProfilePictureForm(request.POST, request.FILES, instance=user_profile)

        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            return redirect("profile")
    else:
        user_form = ProfileUpdateForm(instance=request.user)
        profile_form = ProfilePictureForm(instance=user_profile)

    # Pass the user_profile to the template so we can display its picture
    return render(request, "users/profile.html", {
        "user_form": user_form,
        "profile_form": profile_form,
        "user_profile": user_profile,  # include in context
    })
