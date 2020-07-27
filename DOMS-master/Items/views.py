from django.shortcuts import render, redirect
from .models import Items, Customers
from .forms import ItemForm, CustomerForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required

@login_required
def index(request):
    items = Items.objects.all()
    return render(request, 'index.html', {'items': items})

@login_required
def show(request, order_id):
    item = Items.objects.filter(id=order_id)
    return render(request, 'show.html', {'item': item})

@login_required
def new(request):
    if request.POST:
        iform = ItemForm(request.POST)
        if iform.is_valid():
            if iform.save():
                return redirect('/', messages.success(request, 'Order was successfully created.', 'alert-success'))
            else:
                return redirect('/', messages.error(request, 'Data is not saved', 'alert-danger'))
        else:
            return redirect('/', messages.error(request, 'Form is not valid', 'alert-danger'))
    else:
        iform = ItemForm()
        return render(request, 'new.html', {'iform':iform})


@login_required
def customer(request):
    if request.POST:
        cform = CustomerForm(request.POST)
        if cform.is_valid():
            if cform.save():
                return redirect('/', messages.success(request, 'Order was successfully created.', 'alert-success'))
            else:
                return redirect('/', messages.error(request, 'Data is not saved', 'alert-danger'))
        else:
            return redirect('/', messages.error(request, 'Form is not valid', 'alert-danger'))
    else:
        cform = CustomerForm()
        return render(request, 'customer.html', {'cform':cform})


@login_required
def customer_index(request):
    customers = Customers.objects.all()
    return render(request, 'customer_index.html', {'customers': customers})

@login_required
def edit(request, order_id):
    item = Items.objects.get(id=order_id)
    if request.POST:
        iform = ItemForm(request.POST, instance=item)
        if iform.is_valid():
            if iform.save():
                return redirect('/', messages.success(request, 'Order was successfully updated.', 'alert-success'))
            else:
                return redirect('/', messages.error(request, 'Data is not saved', 'alert-danger'))
        else:
            return redirect('/', messages.error(request, 'Form is not valid', 'alert-danger'))
    else:
        iform = ItemForm(instance=item)
        return render(request, 'edit.html', {'iform':iform})

@login_required
def destroy(request, order_id):
    item = Items.objects.get(id=order_id)
    item.delete()
    return redirect('/', messages.success(request, 'Order was successfully deleted.', 'alert-success'))
