from django import forms
from .models import Activity, Deal, Contact, Note



from django import forms


class BootstrapFormMixin:
    """
    Adds Bootstrap CSS classes to Django form fields automatically.
    Works with ModelForm and regular Form.
    """

    def _apply_bootstrap(self):
        for name, field in self.fields.items():
            widget = field.widget

            # Checkbox
            if isinstance(widget, forms.CheckboxInput):
                existing = widget.attrs.get("class", "")
                widget.attrs["class"] = (existing + " form-check-input").strip()
                continue

            # Select dropdown
            if isinstance(widget, (forms.Select, forms.SelectMultiple)):
                existing = widget.attrs.get("class", "")
                widget.attrs["class"] = (existing + " form-select").strip()
                continue

            # Everything else: text/number/email/date/etc.
            existing = widget.attrs.get("class", "")
            widget.attrs["class"] = (existing + " form-control").strip()

            # Optional: placeholders based on label
            if not widget.attrs.get("placeholder") and field.label:
                widget.attrs["placeholder"] = field.label



class ActivityForm(BootstrapFormMixin, forms.ModelForm):
    class Meta:
        model = Activity
        fields = ["activity_type", "subject", "deal", "contact", "due_date", "is_done"]

    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop("user", None)
        super().__init__(*args, **kwargs)

        # Filter deals to current user
        if self.user and self.user.is_authenticated:
            self.fields["deal"].queryset = Deal.objects.filter(owner=self.user).order_by("-created_at")
        else:
            self.fields["deal"].queryset = Deal.objects.none()

        self.fields["contact"].queryset = Contact.objects.all().order_by("first_name", "last_name")

        # ✅ Apply Bootstrap classes
        self._apply_bootstrap()

    def clean(self):
        cleaned_data = super().clean()
        deal = cleaned_data.get("deal")
        contact = cleaned_data.get("contact")

        if not deal and not contact:
            raise forms.ValidationError(
                "Please link this activity to at least a Deal or a Contact."
            )
        return cleaned_data





class NoteForm(BootstrapFormMixin, forms.ModelForm):
    class Meta:
        model = Note
        fields = ["contact", "deal", "body"]

    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop("user", None)
        super().__init__(*args, **kwargs)

        if self.user and self.user.is_authenticated:
            self.fields["deal"].queryset = Deal.objects.filter(owner=self.user).order_by("-created_at")
        else:
            self.fields["deal"].queryset = Deal.objects.none()

        self.fields["contact"].queryset = Contact.objects.all().order_by("first_name", "last_name")

        # ✅ Apply Bootstrap classes
        self._apply_bootstrap()

    def clean(self):
        cleaned_data = super().clean()
        deal = cleaned_data.get("deal")
        contact = cleaned_data.get("contact")

        if not deal and not contact:
            raise forms.ValidationError(
                "Please attach this note to at least a Deal or a Contact."
            )
        return cleaned_data



from .models import Company, Contact, Deal


class CompanyForm(BootstrapFormMixin, forms.ModelForm):
    class Meta:
        model = Company
        fields = ["name", "industry", "website", "phone", "location"]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._apply_bootstrap()


class ContactForm(BootstrapFormMixin, forms.ModelForm):
    class Meta:
        model = Contact
        fields = ["company", "first_name", "last_name", "email", "phone", "position"]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._apply_bootstrap()


class DealForm(BootstrapFormMixin, forms.ModelForm):
    class Meta:
        model = Deal
        fields = ["company", "contact", "title", "stage", "amount", "expected_close_date"]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._apply_bootstrap()
