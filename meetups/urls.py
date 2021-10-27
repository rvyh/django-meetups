from django.urls import path
from . import views

urlpatterns = [
    # domain.com/meetups
    path('', views.index, name='all-meetups'),
    path('<slug:meetup_slug>/success', views.confirm_registration, name='confirm-registration'),
    # domain.com/meetups/<dynamic-path>
    path('<slug:meetup_slug>', views.meetup_details, name='meetup-details')

]
