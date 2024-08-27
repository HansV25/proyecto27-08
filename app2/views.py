from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def index(request):
    return HttpResponse("<h1>soy el index de la app2</h1>")

def vista1(request):
    html="""
    <h1>hola soy app2</h1>
    <ol>lista</ol>
    <ol>lista</ol>
    <ol>lista</ol>
    <ol>lista</ol>
    <a href="/pagina2/index">Volver</a>
    """
    return HttpResponse(html)