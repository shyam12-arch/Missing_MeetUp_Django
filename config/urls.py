from django.contrib import admin
from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

# from apps.auth import *
from apps.auth import RegisterView, ProtectedView
from apps.reports import views

urlpatterns = [
    path("admin/", admin.site.urls),

    # User Registration
    path("api/register/", RegisterView.as_view(), name="register"),

    # JWT Token Endpoints
    path("api/token/", TokenObtainPairView.as_view(), name="token_obtain_pair"),  # Login
    path("api/token/refresh/", TokenRefreshView.as_view(), name="token_refresh"), # Refresh token

    # Protected Route
    path("api/protected/", ProtectedView.as_view(), name="protected"),
    path('find/',views.ReportMissingPersonView.as_view()),
]

