from django.contrib import admin
from .models import Company, Contact, Deal, Activity, Note

# Register your models here.

@admin.register(Company)
class CompanyAdmin(admin.ModelAdmin):
    list_display = ('name', 'industry', 'phone', 'location', 'created_at')
    search_fields = ('name', 'industry', 'phone', 'location')
    ordering = ('name',)
    
    
@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'company', 'email', 'phone', 'position', 'created_at')
    list_filter = ('company',)
    search_fields = ('first_name', 'last_name', 'email', 'phone', 'position', 'company__name')
    ordering = ('last_name', 'first_name')
    
    
@admin.register(Deal)
class DealAdmin(admin.ModelAdmin):
    list_display = ('title', 'company', 'contact', 'amount', 'stage', 'expected_close_date', 'owner', 'created_at')
    list_filter = ('stage', 'company')
    search_fields = ('title', 'company__name', 'contact__first_name', 'contact__last_name')
    ordering = ('-created_at',)
    
@admin.register(Activity)
class ActivityAdmin(admin.ModelAdmin):
    list_display = ('activity_type','subject', 'due_date', 'is_done', 'created_at')
    list_filter = ('activity_type', 'is_done')
    search_fields = ('subject', 'deal__title', 'contact__first_name', 'contact__last_name')
    ordering = ('-created_at',)
    
    
@admin.register(Note)
class NoteAdmin(admin.ModelAdmin):
    list_display = ('short_body', 'contact', 'deal', 'created_at')
    search_fields = ('body', 'contact__first_name', 'contact__last_name', 'deal__title')
    ordering = ('-created_at',)
    
    @admin.display(description='Body')
    def short_body(self, obj):
        return obj.body[:50]