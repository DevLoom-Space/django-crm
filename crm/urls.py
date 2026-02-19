from django.urls import path
from .views import DealBoardView

from .views import(
    CompanyListView, 
    CompanyDetailView, 
    CompanyCreateView, 
    CompanyUpdateView, 
    CompanyDeleteView,
    ContactListView, 
    ContactDetailView, 
    ContactCreateView,
    ContactUpdateView, 
    ContactDeleteView,
    DealListView, 
    DealDetailView, 
    DealCreateView,
    DealUpdateView, 
    DealDeleteView,
    ActivityListView, 
    ActivityDetailView, 
    ActivityCreateView,
    ActivityUpdateView, 
    ActivityDeleteView,
    NoteListView, 
    NoteDetailView, 
    NoteCreateView,
    NoteUpdateView, 
    NoteDeleteView
)


urlpatterns = [
    path('companies/', CompanyListView.as_view(), name='company_list'),
    path("companies/new/", CompanyCreateView.as_view(), name='company_create'),
    path('companies/<int:pk>/', CompanyDetailView.as_view(), name='company_detail'),
    path('companies/<int:pk>/edit/', CompanyUpdateView.as_view(), name='company_update'),
    path('companies/<int:pk>/delete/', CompanyDeleteView.as_view(), name='company_delete'),
    
    
    path('contacts/', ContactListView.as_view(), name='contact_list'),
    path("contacts/new/", ContactCreateView.as_view(), name='contact_create'),
    path('contacts/<int:pk>/', ContactDetailView.as_view(), name='contact_detail'),
    path('contacts/<int:pk>/edit/', ContactUpdateView.as_view(), name='contact_update'),
    path('contacts/<int:pk>/delete/', ContactDeleteView.as_view(), name='contact_delete'),

    path('deals/', DealListView.as_view(), name='deal_list'),
    path("deals/new/", DealCreateView.as_view(), name='deal_create'),
    path('deals/<int:pk>/', DealDetailView.as_view(), name='deal_detail'),
    path('deals/<int:pk>/edit/', DealUpdateView.as_view(), name='deal_update'),
    path('deals/<int:pk>/delete/', DealDeleteView.as_view(), name='deal_delete'),

    path('activities/', ActivityListView.as_view(), name='activity_list'),
    path("activities/new/", ActivityCreateView.as_view(), name='activity_create'),
    path('activities/<int:pk>/', ActivityDetailView.as_view(), name='activity_detail'),
    path('activities/<int:pk>/edit/', ActivityUpdateView.as_view(), name='activity_update'),
    path('activities/<int:pk>/delete/', ActivityDeleteView.as_view(), name='activity_delete'),


    path('notes/', NoteListView.as_view(), name='note_list'),
    path("notes/new/", NoteCreateView.as_view(), name='note_create'),
    path('notes/<int:pk>/', NoteDetailView.as_view(), name='note_detail'),
    path('notes/<int:pk>/edit/', NoteUpdateView.as_view(), name='note_update'),
    path('notes/<int:pk>/delete/', NoteDeleteView.as_view(), name='note_delete'),


    path("deals/board/", DealBoardView.as_view(), name="deal_board"),

]

