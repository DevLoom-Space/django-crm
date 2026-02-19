from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import (
    ListView, DetailView, CreateView, UpdateView, DeleteView
)
from crm.models import Company, Contact, Deal, Activity, Note

from .mixins import OwnerDealQuerysetMixin


from .forms import CompanyForm, ContactForm, DealForm, ActivityForm, NoteForm


# Create your views here.
class CompanyListView(LoginRequiredMixin, ListView):
    model = Company
    template_name = 'crm/company_list.html'
    context_object_name = 'companies'
    paginate_by = 10    
    ordering = ['name']
    

class CompanyDetailView(LoginRequiredMixin, DetailView):
    model = Company
    template_name = 'crm/company_detail.html'
    context_object_name = 'company'


class CompanyCreateView(LoginRequiredMixin, CreateView):
    model = Company
    template_name = "crm/company_form.html"
    form_class = CompanyForm
    success_url = reverse_lazy("company_list")


class CompanyUpdateView(LoginRequiredMixin, UpdateView):
    model = Company
    template_name = "crm/company_form.html"
    form_class = CompanyForm
    success_url = reverse_lazy("company_list")

    

class CompanyDeleteView(LoginRequiredMixin, DeleteView):
    model = Company
    template_name = 'crm/company_confirm_delete.html'
    success_url = reverse_lazy('company_list')
    
    
    
    
    
    
    
    
    
    
class ContactListView(LoginRequiredMixin, ListView):
    model = Contact
    template_name = 'crm/contact_list.html'
    context_object_name = 'contacts'
    paginate_by = 10    
    ordering = ['last_name', 'first_name']
    
    
class ContactDetailView(LoginRequiredMixin, DetailView):
    model = Contact
    template_name = 'crm/contact_detail.html'
    context_object_name = 'contact'
    
class ContactCreateView(LoginRequiredMixin, CreateView):
    model = Contact
    template_name = "crm/contact_form.html"
    form_class = ContactForm
    success_url = reverse_lazy("contact_list")


class ContactUpdateView(LoginRequiredMixin, UpdateView):
    model = Contact
    template_name = "crm/contact_form.html"
    form_class = ContactForm
    success_url = reverse_lazy("contact_list")

    
    
class ContactDeleteView(LoginRequiredMixin, DeleteView):
    model = Contact
    template_name = 'crm/contact_confirm_delete.html'
    success_url = reverse_lazy('contact_list')                
    
    


class DealListView(LoginRequiredMixin, ListView):
    model = Deal
    template_name = "crm/deal_list.html"
    context_object_name = "deals"
    paginate_by = 10
    ordering = ["-created_at"]

    def get_queryset(self):
        return Deal.objects.filter(owner=self.request.user)



class DealDetailView(OwnerDealQuerysetMixin, DetailView):
    model = Deal
    template_name = "crm/deal_detail.html"
    context_object_name = "deal"

class DealCreateView(LoginRequiredMixin, CreateView):
    model = Deal
    template_name = "crm/deal_form.html"
    form_class = DealForm
    success_url = reverse_lazy("deal_list")

    def form_valid(self, form):
        form.instance.owner = self.request.user
        return super().form_valid(form)


class DealUpdateView(OwnerDealQuerysetMixin, UpdateView):
    model = Deal
    template_name = "crm/deal_form.html"
    form_class = DealForm
    success_url = reverse_lazy("deal_list")




class DealDeleteView(OwnerDealQuerysetMixin, DeleteView):
    model = Deal
    template_name = "crm/deal_confirm_delete.html"
    success_url = reverse_lazy("deal_list")




class ActivityListView(LoginRequiredMixin, ListView):
    model = Activity
    template_name = "crm/activity_list.html"
    context_object_name = "activities"
    paginate_by = 10
    ordering = ['is_done', 'due_date','-created_at']
    
    def get_queryset(self):
        qs = super().get_queryset()
        return qs.filter(deal__owner=self.request.user).order_by('is_done', 'due_date', '-created_at')



class ActivityDetailView(LoginRequiredMixin, DetailView):
    model = Activity
    template_name = "crm/activity_detail.html"
    context_object_name = "activity"
    
    
class ActivityCreateView(LoginRequiredMixin, CreateView):
    model = Activity
    template_name = "crm/activity_form.html"
    form_class = ActivityForm
    success_url = reverse_lazy("activity_list")

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs["user"] = self.request.user
        return kwargs


class ActivityUpdateView(LoginRequiredMixin, UpdateView):
    model = Activity
    template_name = "crm/activity_form.html"
    form_class = ActivityForm
    success_url = reverse_lazy("activity_list")

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs["user"] = self.request.user
        return kwargs

    
    
class ActivityDeleteView(LoginRequiredMixin, DeleteView):
    model = Activity
    template_name = "crm/activity_confirm_delete.html"
    success_url = reverse_lazy("activity_list")    




class NoteListView(LoginRequiredMixin, ListView):
    model = Note
    template_name = "crm/note_list.html"
    context_object_name = "notes"
    paginate_by = 10

    def get_queryset(self):
        # Notes linked to deals owned by current user
        qs = Note.objects.filter(deal__owner=self.request.user).select_related("deal", "contact")
        return qs.order_by("-created_at")  # ✅ Notes only need created_at ordering


    
    
class NoteDetailView(LoginRequiredMixin, DetailView):
    model = Note
    template_name = "crm/note_detail.html"
    context_object_name = "note"
    
    
class NoteCreateView(LoginRequiredMixin, CreateView):
    model = Note
    template_name = "crm/note_form.html"
    form_class = NoteForm
    success_url = reverse_lazy("note_list")

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs["user"] = self.request.user
        return kwargs


class NoteUpdateView(LoginRequiredMixin, UpdateView):
    model = Note
    template_name = "crm/note_form.html"
    form_class = NoteForm
    success_url = reverse_lazy("note_list")

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs["user"] = self.request.user
        return kwargs

    
    
    
class NoteDeleteView(LoginRequiredMixin, DeleteView):
    model = Note
    template_name = "crm/note_confirm_delete.html"
    success_url = reverse_lazy("note_list")
    
    
    





from django.views.generic import TemplateView
from django.db.models import Q
from .models import Deal


class DealBoardView(LoginRequiredMixin, TemplateView):
    template_name = "crm/deal_board.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        user = self.request.user

        # Optional search
        query = self.request.GET.get("q", "").strip()

        deals_qs = Deal.objects.filter(owner=user).select_related("company", "contact")

        if query:
            deals_qs = deals_qs.filter(
                Q(title__icontains=query) |
                Q(company__name__icontains=query) |
                Q(contact__first_name__icontains=query) |
                Q(contact__last_name__icontains=query)
            )

        # Order deals (newest first)
        deals_qs = deals_qs.order_by("-created_at")

        # Get stage choices safely (support either STAGES or STAGE_CHOICES)
        stage_choices = getattr(Deal, "STAGES", None) or getattr(Deal, "STAGE_CHOICES", None)

        columns = []
        for stage_key, stage_label in stage_choices:
            columns.append({
                "key": stage_key,
                "label": stage_label,
                "deals": [d for d in deals_qs if d.stage == stage_key],
            })

        context["columns"] = columns
        context["q"] = query
        context["total_deals"] = deals_qs.count()

        return context
