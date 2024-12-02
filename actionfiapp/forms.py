from django import forms
from .models import Booking

class dataInput(forms.DateInput):
    input_type = 'date'

class BookingForms(forms.ModelForm):
    class Meta:
        model = Booking
        fields = '__all__'
        
        widgets = {  
            'booking_date': dataInput(),
            }
        labels = {
            'p_name' :"Patient name",
            'p_phone':"Patient phone" ,
            'p_email' :"Patient email",
            'doc_name' :"doctor name",
            'booking_date' :"Bookings Date",
        }
