from django.shortcuts import render
from django.http import HttpResponse
from .models import product,Contact,Orders,OrdersUpdate
from math import ceil
import json
# Create your views here.
def index(request):
    products = product.objects.all()
    #print(products)

    # params = {'no_of_slide':nSlides,'range':range(1,nSlides) ,'product':products}
    #allprods=[[products,range(1,nSlides),nSlides],
    #         [products,range(1,nSlides),nSlides]]


    allprods=[]
    catprods =product.objects.values('category','id')
    cats = {item['category'] for item in catprods}
    for cat in cats:
        prod = product.objects.filter(category=cat)
        n = len(products)
        nSlides = n // 4 + ceil((n / 4) - (n // 4))
        allprods.append([prod,range(1,nSlides),nSlides])

    params = {'allprods': allprods}
    return render(request,'WebKart/index.html',params)

def about(request):
    return render(request,'WebKart/about.html')

def contact(request):
    thank = False
    if request.method == 'POST':
        name = request.POST.get('name','none')
        email = request.POST.get('email','none')
        city = request.POST.get('city','none')
        state = request.POST.get('state','none')
        mobile = request.POST.get('mobile','none')
        suggestion = request.POST.get('suggestion', 'none')
        contact = Contact(name=name,email=email,city=city,state=state,mobile=mobile,suggestion=suggestion)
        contact.save()
        thank = True
    return render(request,'WebKart/contact.html',{'thank':thank})

def tracker(request):
    if request.method=="POST":
        orderId = request.POST.get('orderId', '')
        email = request.POST.get('email', '')
        try:
            order = Orders.objects.filter(order_id=orderId, email=email)
            if len(order)>0:
                update = OrdersUpdate.objects.filter(order_id=orderId)
                updates = []
                for item in update:
                    updates.append({'text': item.update_desc, 'time': item.timestamp})
                    response = json.dumps([updates, order[0].items_json], default=str)
                return HttpResponse(response)
            else:
                return HttpResponse('{}')
        except Exception as e:
            return HttpResponse('{}')

    return render(request, 'WebKart/tracker.html')



def search(request):
    return render(request,'WebKart/search.html')

def productview(request, myid):
    #managing Products
    pname = ''
    products = product.objects.all()
    allprods = []
    Product = product.objects.filter(id=myid)
    catprods = product.objects.values('category', 'id')
    cats = {item['category'] for item in catprods}
    print(cats)
    for cat in cats:
        prod = product.objects.filter(category=cat)
        n = len(products)
        nSlides = n // 4 + ceil((n / 4) - (n // 4))
        allprods.append([prod,range(1,nSlides),nSlides])

    return render(request,'WebKart/products.html',{'product':Product[0],'allprods':allprods})

def checkout(request):
    if request.method == 'POST':
        items_json = request.POST.get('itemsjson', '')
        name = request.POST.get('name', 'none')
        email = request.POST.get('email', 'none')
        address = request.POST.get('address1', 'none') + '' + request.POST.get('address2', 'none')
        city = request.POST.get('city', 'none')
        state = request.POST.get('state', 'none')
        zip_code = request.POST.get('zip_code', 'none')
        phone = request.POST.get('phone', 'none')

        order = Orders(items_json=items_json,name=name, email=email,address=address, city=city, state=state, zip_code=zip_code, phone=phone)
        order.save()
        update = OrdersUpdate(order_id=order.order_id,update_desc="Under Processing!")
        update.save()
        thank = True
        id = order.order_id
        return render(request, 'WebKart/checkout.html',{'thank':thank,'id':id})
    return render(request, 'WebKart/checkout.html')


