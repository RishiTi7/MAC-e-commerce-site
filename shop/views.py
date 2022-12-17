from django.http import HttpResponse
from django.shortcuts import render
from .models import Product, Contact, Orders, orderUpdate
from math import ceil
import json

# Create your views here.
def index(request):
    # products = Product.objects.all()
    # n = len(products)
    # nSlides = n // 4 + ceil((n/4)-(n//4))
    # params = {'no_of_slides' : nSlides, 'range' : range (1,nSlides),'product' : products}
    # allprods = [[products, range(1, nSlides), nSlides],
    #  [products, range(1, nSlides), nSlides]]
    allprods = []
    catprods = Product.objects.values("category", "id")
    cats = {item["category"] for item in catprods}
    for cat in cats:
        prod = Product.objects.filter(category=cat)
        n = len(prod)
        nSlides = n // 4 + ceil((n / 4) - (n // 4))
        allprods.append([prod, range(1, nSlides), nSlides])
    params = {"allprods": allprods}
    return render(request, "shop/index.html", params)


def about(request):
    return render(request, "shop/about.html")


def basic(request):
    return render(request, "shop/basic.html")


def contact(request):
    if request.method == "POST":

        name = request.POST.get("name", "")
        email = request.POST.get("email", "")
        phone = request.POST.get("phone", "")
        message = request.POST.get("desc", "")
        contact = Contact(name=name, email=email, phone=phone, message=message)
        contact.save()

    return render(request, "shop/contact.html")


def tracker(request):
    if request.method == "POST":

        orderId = request.POST.get("orderId", "")
        email = request.POST.get("email", "")
        try:
            order = Orders.objects.filter(order_id=orderId, email=email)
            if len(order) > 0:
                update = orderUpdate.objects.filter(order_id=orderId)
                updates = []
                for item in update:
                    updates.append({"text": item.update_desc, "time": item.timestamp})
                    response = json.dumps(updates, default=str)
                return HttpResponse(response)
            else:
                return HttpResponse("{}")
        except Exception as e:
            return HttpResponse("{}")

    return render(request, "shop/tracker.html")


def searchMatch(query, item):
    if (
        query in item.desc.lower()
        or query in item.product_name.lower()
        or query in item.category.lower()
    ):
        return True
    else:
        return False


def search(request):
    query = request.GET.get("search")
    allprods = []
    catprods = Product.objects.values("category", "id")
    cats = {item["category"] for item in catprods}
    for cat in cats:
        prodtemp = Product.objects.filter(category=cat)
        prod = [item for item in prodtemp if searchMatch(query, item)]
        n = len(prod)
        nSlides = n // 4 + ceil((n / 4) - (n // 4))
        if len(prod) != 0:
            allprods.append([prod, range(1, nSlides), nSlides])
    params = {"allprods": allprods}
    if len(allprods) == 0 or len(query)< 2:
        params = {'msg':"Could not find the product"}
    return render(request, "shop/search.html", params)


def productview(request, id):
    # to fetch the products using the id
    product = Product.objects.filter(id=id)
    return render(request, "shop/productview.html", {"product": product[0]})


def checkout(request):
    if request.method == "POST":

        items_json = request.POST.get("itemsjson", "")
        name = request.POST.get("name", "")
        amount = request.POST.get("amount", "")
        email = request.POST.get("email", "")
        phone = request.POST.get("phone", "")
        address = (
            request.POST.get("address1", "") + " " + request.POST.get("address2", "")
        )
        state = request.POST.get("state", "")
        city = request.POST.get("city", "")
        zip_code = request.POST.get("zip_code", "")

        Order = Orders(
            name=name,
            items_json=items_json,
            email=email,
            amount=amount,
            phone=phone,
            address=address,
            state=state,
            city=city,
            zip_code=zip_code,
        )
        Order.save()
        update = orderUpdate(
            order_id=Order.order_id, update_desc="The order has been placed"
        )
        update.save()
        thank = True
        id = Order.order_id
        return render(request, "shop/checkout.html", {"thank": thank, "id": id})
    return render(request, "shop/checkout.html")
