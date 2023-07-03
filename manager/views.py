from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import *
from .forms import OrderForm ,UserForm, ProfileForm

from django.forms import inlineformset_factory
from .filters import OrderFilter
from django.contrib import messages

from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .decorators import unauthenticated, allowed_user, admin_only

from django.contrib.auth.models import Group



@login_required(login_url='login')
@allowed_user(allowed_roles=['customer'])
def settingsPage(request):
    customer = request.user.customer
    form = ProfileForm(instance=customer)

    if request.method == 'POST':
        form = ProfileForm(request.POST,request.FILES,instance=customer)
        if form.is_valid():
            form.save()
    context ={'form':form}
    return render(request,'manager/settings.html',context)


@login_required(login_url='login')
@allowed_user(allowed_roles=['customer'])
def userPage(request):
    order = request.user.customer.order_set.all()

    order_pending = order.filter(status='Pending').count()
    order_delivered = order.filter(status='Delivered').count()

    total = order.count()

    myfilter = OrderFilter(request.GET, queryset=order)

    order = myfilter.qs

    context = {'order':order,'myfilter':myfilter,'order_pending':order_pending,'order_delivered':order_delivered,'total':total}
    return render(request,'manager/user.html',context)

@login_required(login_url='login')
@admin_only
def home(request):
    customer = Customer.objects.all()
    order_pending = Order.objects.filter(status='Pending').count()
    order_delivered = Order.objects.filter(status='Delivered').count()
    order = Order.objects.all()
    total =order.count()

    context = {
        'customer': customer,
        'order_pending': order_pending,
        'order_delivered': order_delivered,
        'total':total,
        'order':order,
    }



    return render(request,'manager/dashboard.html',context)
@login_required(login_url='login')
@allowed_user(allowed_roles=['admin'])
def customer(request,pk_test):
    customer= Customer.objects.get(id=pk_test)
    order = customer.order_set.all()
    total = order.count()

    myfilter = OrderFilter(request.GET,queryset=order)

    order= myfilter.qs



    context ={'customer':customer,'order':order,'total':total,'myfilter':myfilter}

    return render(request,'manager/customer.html',context)

@login_required(login_url='login')
@allowed_user(allowed_roles=['admin'])
def products(request):
    products = Product.objects.all()
    context = {
        'products':products
    }


    return render(request, 'manager/products.html',context)

@login_required(login_url='login')
@allowed_user(allowed_roles=['admin'])
def create_order(request,pk):
    OrderFormSet = inlineformset_factory(Customer,Order,fields=('product','status'),extra=10)
    customer = Customer.objects.get(id=pk)
    #orderform = OrderForm(initial={'customer':customer})
    formset = OrderFormSet()
    if request.method == 'POST':
        formset = OrderFormSet(request.POST,instance=customer)
        if formset.is_valid():
            formset.save()
            return redirect('/')




    context = {'formset':formset}
    return render(request, 'manager/create.html', context)

@login_required(login_url='login')
@allowed_user(allowed_roles=['admin'])
def update(request,pk):
    order = Order.objects.get(id=pk)
    orderform = OrderForm(instance=order)
    if request.method == 'POST':
        orderform = OrderForm(request.POST, instance=order)
        if orderform.is_valid():
            orderform.save()
            return redirect('/')

    context = {'orderform':orderform}
    return render(request, 'manager/create.html', context)
@login_required(login_url='login')
@allowed_user(allowed_roles=['admin'])
def delete(request,pk):
    order = Order.objects.get(id = pk)
    if request.method =='POST':
        order.delete()
        return redirect('/')


    context = {'order':order}
    return render(request, 'manager/delete.html', context)

@unauthenticated
def loginPage(request):

    if request.method == 'POST':
        password = request.POST.get('password')
        username = request.POST.get('username')

        user = authenticate(request,password=password,username=username)

        if user is not None:
            login(request,user)
            return redirect('home')
        else:
            messages.info(request,'you entered a wrong password or username')


    context={}
    return render(request, 'manager/login.html', context)

def registerPage(request):
    form = UserForm()
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            user=form.save()



            messages.success(request,'You have successfully created an account')


            return redirect('login')

    context = {'form':form}
    return render(request, 'manager/register.html', context)

def logoutPage(request):
    logout(request)
    return redirect('login')


