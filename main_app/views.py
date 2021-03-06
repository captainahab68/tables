from django.shortcuts import redirect, render
from django.http import HttpResponseRedirect
from .models import *
from .forms import *
#Math functions (I know they shouldn't be here but I couldn't get script.py to work)
def subtot(order):
    subtot = 0
    order.subtot = 0
    for item in order.items.all():
        subtot += item.price
    order.subtot = subtot
    order.save()

def calc(table_id):
    t = Table.objects.get(id=table_id)
    t.subtot = 0
    for order in t.orders.all():
        t.subtot += order.subtot
    t.tax = float(t.subtot) * 0.0725
    t.bill = float(t.subtot) + float(t.tax)
    t.grat15 = float(t.bill) * 0.15
    t.grat18 = float(t.bill) * 0.18
    t.grat20 = float(t.bill) * 0.2
    t.save()

# Create your views here.
def home(request):
    tables = Table.objects.all()
    if request.method == 'POST':
        form = TableForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('/')
    else:
        table_form = TableForm()
        order_form = OrderForm()
        return render(request, 'tables.html', {'table_form': table_form, 'order_form': order_form, 'tables': tables})
def menu(request):
    pass

def table_detail(request, table_id):
    pass

def table_new(request):
    if request.method == 'POST':
        form = TableForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('/tables/')
    else:
        form = TableForm()
        return render(request, 'table_new.html',{ 'form': form})

def table_close(request, table_id):
    table = Table.objects.get(id=table_id)
    return render(request, 'table_close.html', {'table': table})

def order_new(request, table_id):
    form = OrderForm(request.POST)
    if form.is_valid():
        order = form.save()
        subtot(order)
        Table.objects.get(id=table_id).orders.add(order.id)
        calc(table_id)
    return redirect('/')

def order_update(request, order_id, table_id):
    o = Order.objects.get(id=order_id)
    form = OrderForm(request.POST, instance=o)
    if form.is_valid():
        form.save()
        subtot(o)
        calc(table_id)
    return redirect('/')

def order_delete(request, order_id, table_id):
    Order.objects.get(id=order_id).delete()
    calc(table_id)
    return redirect('/')

def table_delete(request, table_id):
    t = Table.objects.get(id=table_id)
    for order in t.orders.all():
        order.delete()
    t.delete()
    return redirect('/')