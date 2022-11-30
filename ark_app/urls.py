from django.urls import path
from .views import *

urlpatterns = [
    path('',index, name='index'),
    path('register/',register, name='register'),
    path('login/',login, name='login'),
    path('doctor_dashboard/',doctor_dashboard, name='doctor_dashboard'),
    path('appointments/',appointments, name='appointments'),
    path('patient_list/',patient_list, name='patient_list'),
    path('patient_profile/',patient_profile, name='patient_profile'),
    path('invoices/',invoices, name='invoices'), 
    path('doctor_profile_settings/',doctor_profile_settings, name='doctor_profile_settings'), 
    path('search/',search, name='search'), 
    path('booking/',booking, name='booking'), 
    path('checkout/',checkout, name='checkout'), 
    path('booking_success/',booking_success, name='booking_success'), 
    path('invoice_view/',invoice_view, name='invoice_view'), 
    path('profile_settings/',profile_settings, name='profile_settings'), 
    path('change_password/',change_password, name='change_password'), 
    path('contact_us/',contact_us, name='contact_us'),

    path('otp_page/',otp_page, name='otp_page'),
    path('doc_otp/',doc_otp, name='doc_otp'),
    path('verify_otp/',verify_otp, name='verify_otp'),
    path('doc_verify_otp/',doc_verify_otp, name='doc_verify_otp'),


    path('doctor_register/',doctor_register, name='doctor_register'), 
    path('doc_profile_update/',doc_profile_update, name='doc_profile_update'), 
    path('doctor_login/',doctor_login, name='doctor_login'), 
    path('book_appointment/',book_appointment, name='book_appointment'), 
    path('approval_apointment/<int:pk>',approval_apointment, name='approval_apointment'), 

    path('logout/',logout, name='logout'), 
    path('doctor_logout/',doctor_logout, name='doctor_logout'), 
]
