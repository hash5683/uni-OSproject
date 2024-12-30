from django.urls import path
from . import views

#App URLs
urlpatterns = [
    path('signup/', views.signup_view, name='signup'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('about/', views.about, name='about'),
    path('case_study/', views.case_study, name='case_study'),
    path('vision/', views.vision, name='vision'),
    path('contact/', views.contact, name='contact'),
]
