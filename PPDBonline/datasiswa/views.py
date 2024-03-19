from django.shortcuts import render

# Create your views here.

from. forms import datasiswaform

def index(request):
    datasiswa_form = datasiswaform()
    datasiswa = {
        'heading': datasiswa,
        'data_form':datasiswa_form,
    }

    return render(request,'index.html', context)

        