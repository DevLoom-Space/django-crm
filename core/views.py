from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import TemplateView
from django.db.models import Count

from crm.models import Company, Contact, Deal, Activity, Note


class HomeView(TemplateView):
    template_name = "core/home.html"


class DashboardView(LoginRequiredMixin, TemplateView):
    template_name = "core/dashboard.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        user = self.request.user

        # Global counts
        context["companies_count"] = Company.objects.count()
        context["contacts_count"] = Contact.objects.count()

        # User-specific deals
        user_deals = Deal.objects.filter(owner=user)
        context["my_deals_count"] = user_deals.count()

        # ✅ Deals by stage (with human-readable labels)
        stage_counts = (
            user_deals.values("stage")
            .annotate(total=Count("id"))
            .order_by("stage")
        )

        # Build mapping: {"lead": "Lead", "qualified": "Qualified", ...}
        stage_label_map = dict(Deal.STAGES)

        # Provide a clean structure for template rendering
        context["my_deals_by_stage"] = [
            {
                "stage_key": row["stage"],
                "stage_label": stage_label_map.get(row["stage"], row["stage"]),
                "total": row["total"],
            }
            for row in stage_counts
        ]

        # Activities linked to user's deals
        my_activities = Activity.objects.filter(deal__owner=user)
        context["my_pending_activities_count"] = my_activities.filter(is_done=False).count()
        context["recent_activities"] = my_activities.order_by("is_done", "due_date", "-created_at")[:8]

        # Notes linked to user's deals
        my_notes = Note.objects.filter(deal__owner=user)
        context["recent_notes"] = my_notes.order_by("-created_at")[:8]

        return context
