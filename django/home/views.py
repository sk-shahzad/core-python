from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib import messages
from .models import Room, Topic, Messege
from .forms import RoomForm
from django.db.models import Q
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required


# rooms = [
#     {'id':1, 'name':'Lets learn python!'},
#     {'id':2, 'name':'design with me'},
#     {'id':3, 'name':'Frontend develper'},
# ]

def loginPage(request):
    page = 'login'
    if request.user.is_authenticated:
        return redirect('home')
    if request.method == 'POST':
        username = request.POST.get('username').lower()
        password = request.POST.get('password')
        # print(f"Username:{username},Password:{password}")
        try:
            user = User.objects.get(username=username)
        except:
            messages.error(request, 'User does not exist')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.error(request, 'Username OR password does not exist')
    context = {'page': page}
    return render(request, 'saleSawari/login_register.html', context)

def logoutUser(request):
    logout(request)
    return redirect('home')

def registerPage(request):
    page = 'register'
    form = UserCreationForm()

    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.username = user.username.lower()
            user.save()
            login(request, user)
            return redirect('home')
        else:
            messages.error(request, 'An error has occured')

    return render(request, 'saleSawari/login_register.html',{'form':form})


def home(request):
    q = request.GET.get('q') if request.GET.get('q') != None else ''
    rooms = Room.objects.filter(Q(topic__name__icontains=q) | 
    Q(name__icontains=q) |
    Q(description__icontains=q) 
    )

    topics = Topic.objects.all()
    room_count = rooms.count()
    room_messages = Messege.objects.filter(Q(room__topic__name__icontains=q))
    
    context = {'rooms': rooms, 'topics': topics, 'room_count':room_count, 'room_messages': room_messages}
    return render(request, 'saleSawari/home.html', context)

def room(request, pk):
    room = Room.objects.get(id=pk)
    room_messages = room.messege_set.all().order_by('-created')
    participants = room.participants.all()
    if request.method =='POST':
        message = Messege.objects.create(
            user=request.user,
            room=room,
            body=request.POST.get('body')
        )
        room.participants.add(request.user)
        return redirect('room',pk=room.id)
    context = {'room': room, 'room_messages': room_messages, 'participants': participants}
    return render(request, 'saleSawari/Room.html', context)

@login_required(login_url='/login')
def createRoom(request):
    form = RoomForm()
    if request.method == 'POST':
        form = RoomForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect ('home')
    context = {'form': form}
    return render(request, 'saleSawari/room_form.html', context)

@login_required(login_url='/login')
def updateRoom(request, pk):
    room = Room.objects.get(id=pk)
    form = RoomForm(instance=room)

    if request.user != room.host:
        return HttpResponse("you are not allowed here")

    if request.method == 'POST':
        form = RoomForm(request.POST, instance=room)
        if form.is_valid():
            form.save()
            return redirect ('home')
    context = {'form': form}
    return render(request, 'saleSawari/room_form.html', context)

@login_required(login_url='/login')
def deleteRoom(request, pk):
    room = Room.objects.get(id=pk)

    if request.user != room.host:
        return HttpResponse("you are not allowed here")

    if request.method == 'POST':
        room.delete()
        return redirect ('home')
    return render(request, 'saleSawari/delete.html', {'obj': room})

@login_required(login_url='/login')
def deleteMessage(request, pk):
    message = Messege.objects.get(id=pk)

    if request.user != message.user:
        return HttpResponse("you are not allowed here")

    if request.method == 'POST':
        message.delete()
        return redirect ('home')
    return render(request, 'saleSawari/delete.html', {'obj': message})