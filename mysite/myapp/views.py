from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def index(response):
	return HttpResponse("<h1>Let's start django!</h1>")

def page1(response):
	return HttpResponse("<h1>Page 1!</h1>")	