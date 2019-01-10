from django.shortcuts import render
from django.http import HttpResponse
import mysql.connector

# Create your views here.
conn = mysql.connector.connect(
  host="localhost",
  user="root",
  passwd="innoraft"
)
conn_cursor = conn.cursor()

def adminHome(response):
    return HttpResponse('admin home')
def addcontent(request):
    return render(request, 'addcontent.html')
def addcontentdb(request):
    return HttpResponse('request')
