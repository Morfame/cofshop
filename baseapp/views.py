from django.shortcuts import render

menus = [
    {'id':1, 'name':'Breakfast Menu'},
    {'id':2, 'name':'Lunch Menu'},
    {'id':3, 'name':'Dinner Menu'},
]

def home(request):
    context = {'menus': menus}
    return render(request, 'baseapp/home.html', context)

def menu(request):
    return render(request, 'baseapp/menu.html')
