from django.shortcuts import render, redirect
from .models import Articles
from .forms import ArticlesForm


# Create your views here.
def data_home(request):
    data = Articles.objects.all()
    return render(request, 'data/data_home.html', {'data': data})

def create(request):
    error = ''
    if request.method == 'POST':
        form = ArticlesForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('data_home')
        else:
            error = 'incorrect'

    form = ArticlesForm()

    datar = {
        'form': form,
        'error': error
    }
    return render(request, 'data/create.html', datar)
