from django.shortcuts import render
from django.http import HttpResponse
from .models import ToDoList, Item
from .forms import CreateNewList
# Create your views here.



def index(response, id):
	ls = ToDoList.objects.get(id = id)

	return render(response, "myapp/list.html", {"ls":ls})

def home(respocd nse):
	return render(response, "myapp/home.html", {})

def create(response):
	if response.method == "POST":
		form = CreateNewList(response.POST)
		if form.is_valid():
			n = form.cleaned_data["name"]
			t = ToDoList(name = n)
			t.save()
		return HttpResponseRedirect("/%i" %t.id) 	

	else:
		form = CreateNewList()
	return render(response, "myapp/create.html", {"form":form})	
