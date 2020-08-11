from django.http import HttpResponse
from django.shortcuts import render


# Create your views here.
def homepage_view(request,*args,**kwargs):
    return render(request,"home.html",{})


def about(request,*args,**kwargs):
    return render(request,"about.html",{})

def contact(request,*args,**kwargs):
    my_contact={
        "name":"Santhosh",
        "Contact":701005242,
        "list":[123,456,789]
    }
    return render(request,"contact.html",my_contact)