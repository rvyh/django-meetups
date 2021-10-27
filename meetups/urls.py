from django.urls import path
from . import views

urlpatterns = [
    # domain.com/meetups
    path('meetups/', views.index, name='all-meetups'),
    path('meetups/success', views.confirm_registration, name='confirm-registration'),
    # domain.com/meetups/<dynamic-path>
    path('meetups/<slug:meetup_slug>', views.meetup_details, name='meetup-details')

]
