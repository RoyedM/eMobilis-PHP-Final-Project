import requests
import json

from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404

from final_app.credentials import LipanaMpesaPpassword, MpesaAccessToken
from .models import Seat
from django.contrib.auth.decorators import login_required


# Create your views here.
def home (request):
    return render(request, 'index.html')

def about (request):
    return render(request, 'about.html')

def bookings (request):
    return render(request, 'bookings.html')

def contact (request):
    return render(request, 'contact.html')

def seat (request):
    return render(request, 'seat.html')

@login_required(login_url='accounts:login')
def seat(request):
    if request.method == 'POST':
        # Create variable to pick the input fields
        seat = Seat(
        # list the input fields here
            name = request.POST['name'],
            email = request.POST['email'],
            phone = request.POST['phone'],
            date = request.POST['date'],
            time = request.POST['time'],
            people = request.POST['people'],
            travel_class = request.POST['travel_class'],
            route = request.POST['route'],
            message = request.POST['message'],
        )
        # save the variable
        seat.save()
        # redirect to a page
        return redirect('final_app:bookings')
    else:
        return render(request, 'seat.html')
    
    
    # retrieve all bookings
def retrieve_bookings(request):
        # retrieve/fetch bookings
        # create a variable to store
        seat = Seat.objects.all()
        context = {
            'seat':seat}
        return render(request, 'bookings.html', context)
    
    # delete
def delete_bookings(request, id):
        # deleting
        seat = Seat.objects.get(id=id)
        seat.delete()
        return redirect("final_app:bookings")

# update
def update_bookings(request, seat_id):
        """update the appointments"""
        seat = get_object_or_404(Seat, id=seat_id)
        """put the condition for the form to update"""
        if request.method == 'POST':
             seat.name = request.POST.get('name')
             seat.email = request.POST.get('email')
             seat.phone = request.POST.get('phone')
             seat.date = request.POST.get('date')
             seat.time = request.POST.get('time')
             seat.people = request.POST.get('people')
             seat.travel_class = request.POST.get('travel_class')
             seat.route = request.POST.get('route')
             seat.message = request.POST.get('message')
             seat.save()

             return redirect("final_app:bookings")
        context = {'seat': seat}
        return render(request, "update_bookings.html", context)



# Adding the mpesa functions

#Display the payment form
def pay(request):
   """ Renders the form to pay """
   return render(request, 'pay.html')


# Generate the ID of the transaction
def token(request):
    """ Generates the ID of the transaction """
    consumer_key = 'tmeHSH7BGxisJ5T5z18LN4AUIAaAETkPD0zWh4TzOFhNdrnN'
    consumer_secret = 'ezB58xQAxmshkEwshsqRGzG29gqFrX8STZwUi1AxdDBMqMxaaPot2msroG2oTcAc'
    api_URL = 'https://sandbox.safaricom.co.ke/oauth/v1/generate?grant_type=client_credentials'

    r = requests.get(api_URL, auth=HTTPBasicAuth(
        consumer_key, consumer_secret))
    mpesa_access_token = json.loads(r.text)
    validated_mpesa_access_token = mpesa_access_token["access_token"]

    return render(request, 'token.html', {"token":validated_mpesa_access_token})


# Send the stk push
def stk(request):
    """ Sends the stk push prompt """
    if request.method =="POST":
        phone = request.POST['phone']
        amount = request.POST['amount']
        access_token = MpesaAccessToken.validated_mpesa_access_token
        api_url = "https://sandbox.safaricom.co.ke/mpesa/stkpush/v1/processrequest"
        headers = {"Authorization": "Bearer %s" % access_token}
        request = {
            "BusinessShortCode": LipanaMpesaPpassword.Business_short_code,
            "Password": LipanaMpesaPpassword.decode_password,
            "Timestamp": LipanaMpesaPpassword.lipa_time,
            "TransactionType": "CustomerPayBillOnline",
            "Amount": amount,
            "PartyA": phone,
            "PartyB": LipanaMpesaPpassword.Business_short_code,
            "PhoneNumber": phone,
            "CallBackURL": "https://sandbox.safaricom.co.ke/mpesa/",
            "AccountReference": "eMobilis",
            "TransactionDesc": "Web Development Charges"
        }
        response = requests.post(api_url, json=request, headers=headers)
        return HttpResponse("Success")
    
