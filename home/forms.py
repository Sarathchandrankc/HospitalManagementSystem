from django import forms


from .models import Booking,Doctors

class DateInput(forms.DateInput):
    input_type = 'date'

class BookingForm(forms.ModelForm):
    class Meta:
        model = Booking
        fields = '__all__'

        widgets = {
            "booking_date": DateInput(attrs={"class":"form-control"}),
            "p_name":forms.TextInput(attrs={"class":"form-control"}),
            "p_phone":forms.TextInput(attrs={"class":"form-control"}),
            # "doc_name":forms.TextInput(attrs={"class":"form-control"}),
            "p_email":forms.TextInput(attrs={"class":"form-control"}),
            
        }

        labels = {
           'p_name':'Patient Name',
           'p_phone':'Phone Number',
           'p_email':'Email',
           'dep_name':'Department Name',
           'doc_name':'Doctor Name',
           'booking_date':'Booking Date',
        }
       