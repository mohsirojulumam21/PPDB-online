from django.shortcuts import render

from. froms import formfield

def index(request):
    form_field = formfield()
    context = {
        'heading': 'Home',
        'data_form': form_field,
    }

    return render(request, 'index.html',context)
