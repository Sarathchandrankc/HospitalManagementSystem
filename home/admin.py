from django.contrib import admin

from .models import Departments, Doctors, Booking
# Register your models here.




class DoctorAdmin(admin.ModelAdmin):
    list_display =  ('id', 'doc_name', 'doc_spec', 'dep_name' ,'doc_image')

class BookingAdmin(admin.ModelAdmin):
    list_display =  ('id', 'p_name', 'p_phone', 'p_email', 'doc_name','booking_date', 'booked_on' )

class DeptAdmin(admin.ModelAdmin):
    list_display =  ('id', 'dep_name','dep_decription')

admin.site.register(Booking, BookingAdmin)

admin.site.register(Doctors,DoctorAdmin) 

admin.site.register(Departments,DeptAdmin)


