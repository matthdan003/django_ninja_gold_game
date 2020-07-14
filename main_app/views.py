from django.shortcuts import render, HttpResponse, redirect

def index(request):
    return render(request, 'index.html')

def process_money(request):
    return redirect('')