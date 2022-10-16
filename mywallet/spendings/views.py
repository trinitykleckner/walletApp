from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import Budget
from .models import Spend

def wallet(request):
    this = Budget.objects.filter(id=1)[0]
    bud = Budget.objects.filter(id=2)[0]
    context = {'budget' : bud}

    if this.food != 0:
        if this.food >= bud.food:
            context['food'] = '2'
        elif this.food >= bud.food - (bud.food*.25):
            context['food'] = '1'
        else:
            context['food'] = '0'
    if this.travel != 0:
        if this.travel >= bud.travel:
            context['travel'] = '2'
        elif this.travel >= 75:
            context['travel'] = '1'
        else:
            context['travel'] = 0
    if this.entertainment != 0:
        if this.entertainment >= bud.entertainment:
            context['entertainment'] = '2'
        elif this.entertainment >= bud.entertainment - (bud.entertainment*.25):
            context['entertainment'] = '1'
        else:
            context['entertainment'] = '0'
    if this.education != 0:
        if this.education >= bud.education:
            context['education'] = '2'
        elif this.education >= bud.education - (bud.education*.25):
            context['education'] = '1'
        else:
            context['education'] = '0'
    if this.bills != 0:
        if this.bills >= bud.bills:
            context['bills'] = '2'
        elif this.bills >= bud.bills - (bud.bills*.25):
            context['bills'] = '1'
        else:
            context['bills'] = '0'
    if this.health != 0:
        if this.health >= bud.health:
            context['health'] = '2'
        elif this.health >= bud.health - (bud.health*.25):
            context['health'] = 1
        else:
            context['health'] = 0
    if this.shopping != 0:
        if this.shopping >= bud.shopping:
            context['shopping'] = 2
        elif this.shopping >= bud.shopping - (bud.shopping*.25):
            context['shopping'] = '1'
        else:
            context['shopping'] = 0

    context['travel'] = 'saljkdaskh'
    context['bills'] = '0'
    context['shopping'] = 1
    context['health'] = '0'
    return render(request, 'WalletData.html', context)

def index(request):
    return render(request, 'index.html', {})
    #return HttpResponse("Your here!")
    budget_list = Budget.objects.all().values()
    #return HttpResponse(budget_list)
    output = ''
    for i in budget_list:
        if output != "": output += ", "
        output += str(i['id'])
    return HttpResponse("Here are your budgets:   "+output)

def detail(request, budget_id):



    return render(request, 'index.html', context)
    return HttpResponse(this)
    return HttpResponse("You're looking at budget %s." % budget_id)
