from django.contrib import admin
from .models import Department,Doctor,Booking

class BookingAdmin(admin.ModelAdmin):
    list_display=('id','p_name','p_phone','doc_name','booking_date','booked_on')

# Register your models here.
admin.site.register(Department)
admin.site.register(Doctor)
admin.site.register(Booking,BookingAdmin)