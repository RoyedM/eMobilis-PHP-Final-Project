from django.urls import path
from . import views

app_name = 'final_app'

urlpatterns = [
    path('', views.home, name="home"),
    path('about/', views.about, name="about"),
    path('bookings/', views.retrieve_bookings, name="bookings"),
    path('contact/', views.contact, name="contact"),
    path('seat/', views.seat, name="seat"),
    path('delete/<int:id>', views.delete_bookings, name="delete_bookings"),
    path('edit/<int:seat_id>', views.update_bookings, name="update_bookings"),
    path('pay/', views.pay, name='pay'), # view the payment form
    path('stk/', views.stk, name='stk'), # send the stk push prompt
    path('token/', views.token, name='token'), # generate the token for that particular transaction




]