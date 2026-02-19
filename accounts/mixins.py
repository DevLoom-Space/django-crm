from django.shortcuts import redirect

class RedirectAuthenticatedUserMixin:
    redirect_url_name = "dashboard"

    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect(self.redirect_url_name)
        return super().dispatch(request, *args, **kwargs)
