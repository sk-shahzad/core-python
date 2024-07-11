from django.shortcuts import render

rooms = [
    {'id':1, 'name':'Lets learn python!'},
    {'id':2, 'name':'design with me'},
    {'id':3, 'name':'Frontend develper'},
]

def home(request):
    context = {'rooms': rooms}
    return render(request, 'saleSawari/home.html', context)

def room(request, pk):
    room = None
    for i in rooms:
        if i['id'] == int(pk):
            room = 1
    context = {'room': room}
    return render(request, 'saleSawari/Room.html', context)
