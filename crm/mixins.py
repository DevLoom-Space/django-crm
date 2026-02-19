from django.contrib.auth.mixins import LoginRequiredMixin


class OwnerDealQuerysetMixin(LoginRequiredMixin):
    """
    Restricts Deal objects to those owned by the logged-in user.
    Protects Detail/Update/Delete views from URL guessing.
    """
    def get_queryset(self):
        qs = super().get_queryset()
        return qs.filter(owner=self.request.user)
