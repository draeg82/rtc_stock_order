from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from stock_order.models import Washer, Product, WasherQueue
from django import forms


def index(request):
    tempList = ['rtc_unit', 'prep_1']
    context = {'all_pages': tempList}
    return render(request, 'stock_order/index.html', context)


def rtc_unit(request):
    if request.method == 'POST':
        queue = WasherQueue()
        queue.volume = request.POST.get("volume", "")
        queue.washer = request.POST.get("washer", "")
        queue.product = request.POST.get("product", "")
        queue.save()

        return HttpResponseRedirect('/stock_order/rtc_unit/')

    washer = Washer.objects.all()
    products = Product.objects.all()
    queues = WasherQueue.objects.all()
    context = {'all_washers': washer, 'all_products': products, 'all_queues': queues}

    return render(request, 'stock_order/rtc_unit.html', context)


def prep_1(request):
    return (HttpResponse("<h2>Prep 1</h2>"))


def deleteFromWashQueue(request):

    if request.method == 'POST':
        queue_id = request.POST.get("itemForDeletePK", "")
        itemToDelete = WasherQueue.objects.get(pk=queue_id)
        itemToDelete.delete()
        return HttpResponseRedirect('/stock_order/rtc_unit/')

def moveQueueItemUp(request):

    if request.method == 'POST':
        queue_id = request.POST.get("moveUp", "")
        itemToMove = WasherQueue.objects.get(pk=queue_id)
        itemToMove.up()
        return HttpResponseRedirect('/stock_order/rtc_unit/')

def moveQueueItemDown(request):

    if request.method == 'POST':
        queue_id = request.POST.get("moveDown", "")
        itemToMove = WasherQueue.objects.get(pk=queue_id)
        itemToMove.down()
        return HttpResponseRedirect('/stock_order/rtc_unit/')
