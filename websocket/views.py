from django.shortcuts import render

# Create your views here.

def boards(request):
    return render(request, 'chat/index.html')

def board(request, room_name):
    return render(request, 'chat/room.html', {"room_name": room_name})