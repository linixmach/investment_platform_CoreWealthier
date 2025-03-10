from django.urls import path
from .views import CustomLoginView, register, client_dashboard, withdraw, purchase_plan, purchase_success,  home, about, transaction, profile, user_logout, pending
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path("register/", register, name="register"),
    path("login/", CustomLoginView.as_view(), name="login"),
    path("logout/", user_logout, name="logout"),
    path("dashboard/", client_dashboard, name="dashboard"),
    path('withdraw/', withdraw, name='withdraw'),
    path('purchase-plan/', purchase_plan, name='purchase_plan'),
    path("purchase-success/", purchase_success, name="purchase_success"),
    path('home/', home, name='home'),
    path('about/', about, name='about'),
    path('contact/', about, name='contact'),
    path('transaction/', transaction, name='transaction'),
    path('profile/', profile, name='profile'),
    path('pending/', pending, name='pending')

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


