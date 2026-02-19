from django.db import models
from django.contrib.auth import get_user_model

# Create your models here.

User = get_user_model()


class Company(models.Model):
    name = models.CharField(max_length=255, unique=True)
    industry = models.CharField(max_length=255, blank=True)
    website = models.URLField(blank=True)
    phone = models.CharField(max_length=20, blank=True)
    location = models.CharField(max_length=255, blank=True)
    
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.name


class Contact(models.Model):
    company = models.ForeignKey(
        Company, 
        related_name='contacts', 
        on_delete=models.CASCADE)
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=20, blank=True)
    position = models.CharField(max_length=255, blank=True)
    
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"{self.first_name} {self.last_name}"
    


class Deal(models.Model):
    STAGES = [
        ('lead', 'Lead'),
        ('qualified', 'Qualified'),
        ('proposal', 'Proposal'),
        ('won', 'Won'),
        ('lost', 'Lost'),
    ]    
    
    company = models.ForeignKey(
        Company,
        on_delete=models.CASCADE,
        related_name='deals'
    )
    
    contact = models.ForeignKey(
        Contact,
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        related_name='deals'
    )
    
    title = models.CharField(max_length=255)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    stage = models.CharField(max_length=20, choices=STAGES, default='lead')
    expected_close_date = models.DateField(null=True, blank=True)
    
    owner = models.ForeignKey(
        User,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='deals_owned'
    )
    
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.title
    
class Activity(models.Model):
    TYPES = [
        ('call', 'Call'),
        ('meeting', 'Meeting'),
        ('email', 'Email'),
        ('followup', 'Follow-up'),
        
    ]   
    deal = models.ForeignKey(
        Deal,
        on_delete=models.CASCADE,
        related_name='activities',
        blank=True,
        null=True
    ) 
    contact = models.ForeignKey(
        Contact,
        on_delete=models.CASCADE,
        related_name='activities',
        blank=True,
        null=True
    )
    
    activity_type = models.CharField(max_length=20, choices=TYPES)
    subject = models.CharField(max_length=255)
    due_date = models.DateTimeField(blank=True, null=True)
    
    is_done = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"{self.get_activity_type_display()}: {self.subject}"
    
    
class Note(models.Model):
    contact = models.ForeignKey(
        Contact,
        on_delete=models.CASCADE,
        related_name='notes',
        blank=True,
        null=True
    )
    deal = models.ForeignKey(
        Deal,
        on_delete=models.CASCADE,
        related_name='notes',
        blank=True,
        null=True
    )
    
    body = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.body[:40]