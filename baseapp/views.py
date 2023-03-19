from django.shortcuts import render

menus = [
    {'id':1, 'name':'Breakfast Menu'},
    {'id':2, 'name':'Lunch Menu'},
    {'id':3, 'name':'Dinner Menu'},
]

def home(request):
    context = {'menus': menus}
    return render(request, 'baseapp/home.html', context)

def menu(request, pk):
    menu = None
    for i in menus:
        if i['id'] == int(pk):
            menu = i

    context = {'menu': menu}
    return render(request, 'baseapp/menu.html', context)
