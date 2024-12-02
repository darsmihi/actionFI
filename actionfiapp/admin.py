from django.contrib import admin
from .models import Department,Doctors,Booking, Role, UserProfile
# Register your models here.
admin.site.register(Department)
admin.site.register(Doctors)
class Bookingadmin(admin.ModelAdmin):
    list_display = ('id', 'p_name', 'p_email', 'doc_name', 'booking_date', 'booked_on')
    
admin.site.register(Booking, Bookingadmin)
admin.site.register(Role)
admin.site.register(UserProfile)

