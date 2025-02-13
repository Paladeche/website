import os
import time
from django.conf import settings
from django.http import FileResponse, HttpResponse
from django.shortcuts import render
import mcstatus
from mcstatus import JavaServer
from .models import Server
import requests

def index(request):
    if request.method == "POST":
        file_path = os.path.join(os.path.join(settings.MEDIA_ROOT, 'paladechejar'), "slt.txt")
        response = FileResponse(open(file_path, 'rb'), as_attachment=True)
        return response
    return render(request, "paladeche/index.html")

def About(request):
    if request.method == "POST":
        file_path = os.path.join(os.path.join(settings.MEDIA_ROOT, 'about'), "Paladèche.drawio")
        response = FileResponse(open(file_path, 'rb'), as_attachment=True)
        return response
    return render(request, "paladeche/about.html")

def status(request):
    servers = Server.objects.all()
    for server in servers:
        MCserver = JavaServer.lookup(server.ip)
        if server.name == "launcher":
            try:
                response = requests.get(server.ip)
                print(response)
                if response.status_code == 200:
                    server.status = response
                    server.latency = round(response.elapsed.total_seconds() * 1000, 1)
            except requests.exceptions.RequestException as e:
                print(f"An error occurred: {e}")
                return False
        else:
            try:
                server.status = MCserver.status()
                server.status.latency = round(server.status.latency, 1)
            except:
                pass

    return render(request, "paladeche/status.html", {
        'servers': servers,
    })