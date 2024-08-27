from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def index(request):
    html="""
    <h1>Soy el index de la app1</h1>
    <h2>Hola!</h2>
    """
    return HttpResponse(html)

def vista1(request):
    html="""
    <h1>Hola</h1>
    <li>lista 1
    <ul>1</ul>
    <ul>2</ul>
    <ul>3</ul>
    </li>
    <li>lista 2</li>
    <li>lista 3</li>
    <li>lista 4</li>
    """
    return HttpResponse(html)