from django.shortcuts import render
from .decorators import mod_only


# Create your views here.
@mod_only
def staff_info(request):
    return render(request, 'staff/staff_info.html')
