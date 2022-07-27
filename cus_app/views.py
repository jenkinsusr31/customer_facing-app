from django.shortcuts import render, HttpResponse
from .models import Customer
#from datetime import datetime
from django.db.models import Q


# Create your views here.
def index(request):
    return render(request, 'index.html')


def all_cus(request):
    cust = Customer.objects.all()
    context = {
        'cust': cust
    }
    print(context)
    return render(request, 'all_cus.html', context)


def add_cus(request):
    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        gender = request.POST['gender']
        phone = int(request.POST['phone'])
        new_cus = Customer(first_name= first_name, last_name=last_name, gender=gender, phone=phone)
        new_cus.save()
        return HttpResponse('Customer added Successfully')
    elif request.method=='GET':
        return render(request, 'add_cus.html')
    else:
        return HttpResponse("An Exception Occured! Customer Has Not Been Added")


def remove_cus(request, cus_id = 0):
    if cus_id:
        try:
            cus_to_be_removed = Customer.objects.get(id=cus_id)
            cus_to_be_removed.delete()
            return HttpResponse("Customer Removed Successfully")
        except:
            return HttpResponse("Please Enter A Valid cus ID")
    cust = Customer.objects.all()
    context = {
        'cust': cust
    }
    return render(request, 'remove_cus.html',context)


def filter_cus(request):
    if request.method == 'POST':
        name = request.POST['name']
        gender = request.POST['gender']
        cust = Customer.objects.all()
        if name:
            cust = cust.filter(Q(first_name__icontains = name) | Q(last_name__icontains = name))
        if gender:
            cust = cust.filter(gender__name__icontains = gender)

        context = {
            'cust': cust
        }
        return render(request, 'view_all_cus.html', context)

    elif request.method == 'GET':
        return render(request, 'filter_cus.html')
    else:
        return HttpResponse('An Exception Occurred')