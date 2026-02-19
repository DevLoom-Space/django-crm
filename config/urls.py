from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views

urlpatterns = [
    path("admin/", admin.site.urls),

    # ✅ auth FIRST (so nothing can shadow them)
    path(
        "login/",
        auth_views.LoginView.as_view(
            template_name="auth/login.html",
            redirect_authenticated_user=True,
        ),
        name="login",
    ),
    path("logout/", auth_views.LogoutView.as_view(), name="logout"),

    # apps
    path("", include("core.urls")),
    path("", include("crm.urls")),
    path("", include("accounts.urls")),
]
