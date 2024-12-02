from django.shortcuts import render
from .forms import BookingForms
from .models import Department,Doctors
from django.http import HttpResponseForbidden
from functools import wraps

def role_required(allowed_roles):
    def decorator(view_func):
        @wraps(view_func)
        def _wrapped_view(request, *args, **kwargs):
            if request.user.is_authenticated:
                user_role = request.user.userprofile.role.name
                if user_role in allowed_roles:
                    return view_func(request, *args, **kwargs)
            return HttpResponseForbidden("You do not have permission to access this page.")
        return _wrapped_view
    return decorator


def index(request):
    # person = {
    #     'name':'Darshan',
    #     'year':'2000',
    #     'place':'calicut'
    # }
    return render(request,"index.html")

def about(request):
    return render(request,"about.html")

def contact(request):
    return render(request,"contact.html")

@role_required(['admin', 'Doctor'])
def doctors(request):
    print(f"Logged in as: {request.user.username}, Role: {request.user.userprofile.role.name}")
    doc_dict={
        'doctors': Doctors.objects.all()
    }
    return render(request,"doctors.html",doc_dict)

def bookings(request):
    if request.method == 'POST':
        form=BookingForms(request.POST)
        if form.is_valid():
            form.save()
            return render(request,"confirmation.html")
    form = BookingForms()
    book_dict={
        'form' : form
    }
    return render(request,"bookings.html",book_dict)

def department(request):
    dept_dict = {
        'dept': Department.objects.all()
    }
    return render(request, "department.html", dept_dict)



